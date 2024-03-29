import json
import re
from fastapi import HTTPException
from openai import APIConnectionError, APIError, APIResponseValidationError, APIStatusError, APITimeoutError, BadRequestError, ConflictError, InternalServerError, NotFoundError, PermissionDeniedError, RateLimitError, AuthenticationError, UnprocessableEntityError
from pydantic import BaseModel
from src.client import LLMClient
from src.config import settings

class PromptInput(BaseModel):
    prompt: str

def handle_api_status_error(e):
    return e.status_code, f"API Status Error: {e.message}"

def handle_api_error(e):
    return 500, f"API Error: {e.message}"

## research better implementations such as using orjson
def sanitize_json_output(json_string):
    pattern = r"{([^}]*)}"
    result = re.search(pattern, json_string)
    if result:
        new_string = json_string[result.start():]
        new_string = new_string[:new_string.rindex("}")] + "}"
        return new_string.strip()

def extractContent(response, json_mode=False) -> str:
    if json_mode:
        try:
            extracted_response = response.choices[0].message.content
            json.loads(extracted_response)
        except json.decoder.JSONDecodeError:
            print("extracted_response was not a proper JSON object: ", extracted_response)
            print("Attempting to sanitize using sanitize_json_output")
            new_extracted_response = sanitize_json_output(extracted_response)
            return new_extracted_response
    return response.choices[0].message.content if response.choices else "No response"

exception_mappings = {
    APITimeoutError: (408, "Request timed out."),
    APIConnectionError: (503, "Trouble connecting to the AI server."),
    BadRequestError: (400, "Invalid request parameters."),
    AuthenticationError: (401, "Authentication failed."),
    PermissionDeniedError: (403, "Insufficient permissions for the request."),
    NotFoundError: (404, "Not found."),
    ConflictError: (409, "Conflict Error."),
    UnprocessableEntityError: (422, "Unprocessable Entity Error"),
    RateLimitError: (429, "Rate limit exceeded."),
    InternalServerError: (500, "Internal server error."),
    APIResponseValidationError: (500, "Response Validation Error."),
    APIStatusError: handle_api_status_error,
    APIError: handle_api_error
}

class LLMPrompt:
    def __init__(self, prompt, system_prompt, config=None, async_client=False, custom_service = settings.default_service):
        self.client = LLMClient(async_client=async_client, config=config, custom_service=custom_service)
        self.async_client = async_client
        self.model = self.client.config.selected_model
        self.prompt = prompt
        self.system_prompt = system_prompt
        self.response = None
        self.chunks_list = []
        self.response_text = ""
        self.messages = [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": self.prompt},
                ]
    
    def getContent(self) -> str:
        return self.response.choices[0].message.content if self.response.choices else "No response"
    
    def _request_arg_builder(self, json_mode, stream, max_tokens):
        request_args = {
            "model": self.model,
            "messages": self.messages,
            "max_tokens": max_tokens
            }
        if json_mode:
            request_args["response_format"] = {"type": "json_object"}
        if stream:
            request_args["stream"] = True
        return request_args
    
    def _handle_request_exception(self, e):
        status_code, detail_msg = exception_mappings.get(type(e), (500, "An unexpected error occurred."))
        detail = f"{detail_msg} {str(e)}"
        raise HTTPException(status_code=status_code, detail=detail)

    async def send_async(self, json_mode=False, stream=False, max_tokens=1024):
        if not self.async_client:
            raise ValueError("Initialized non async OpenAI client. Use send instead")
        request_args = self._request_arg_builder(json_mode,stream,max_tokens)
        try:
            self.response = await self.client.client.chat.completions.create(**request_args)
        except Exception as e:
            self._handle_request_exception(e)
        return self.response
        
    def send(self, json_mode=False, stream=False, max_tokens=1024):
        if self.async_client:
            raise ValueError("Initialized AsyncOpenAI client. Use send_async instead")
        request_args = self._request_arg_builder(json_mode,stream,max_tokens)
        try:
            self.response = self.client.client.chat.completions.create(**request_args)
        except Exception as e:
            self._handle_request_exception(e)
        return self.response

    # unused code below
    # def _print_verbose_output(self, start_time, end_time):
    #     elapsed_time = end_time - start_time
    #     token_count = self._get_token_count()

    #     input_tokens, output_tokens, total_tokens = self._get_token_details()
    #     cost = self._calculate_cost(input_tokens, output_tokens)

    #     # print("Response:", self.response.choices[0].message.content)
    #     print("Tokens used:", token_count)
    #     print(f"Time elapsed: {elapsed_time:.2f} seconds")
    #     print(f"Estimated Cost: ${cost}")

    # def _get_token_count(self):
    #     if hasattr(self.response, 'usage') and hasattr(self.response.usage, 'total_tokens'):
    #         return self.response.usage.total_tokens
    #     return "Token count not available"

    # def _get_token_details(self):
    #     if hasattr(self.response, 'usage'):
    #         input_tokens = self.response.usage.prompt_tokens
    #         output_tokens = self.response.usage.completion_tokens
    #         total_tokens = input_tokens + output_tokens
    #         return input_tokens, output_tokens, total_tokens
    #     return "Unavailable", "Unavailable", "Unavailable"

    # def _calculate_cost(self, input_tokens, output_tokens):
    #     input_token_cost = 0.0005 / 1000  # Cost per input token
    #     output_token_cost = 0.0015 / 1000  # Cost per output token
    #     if isinstance(input_tokens, int) and isinstance(output_tokens, int):
    #         return round((input_tokens * input_token_cost) + (output_tokens * output_token_cost), 5)
    #     return "Cost calculation not available"
    
