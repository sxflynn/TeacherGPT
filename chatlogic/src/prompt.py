import time

class Prompt:
    def __init__(self, client, prompt, system_prompt, verbose=False):
        self.client = client
        self.model = client.model
        self.prompt = prompt
        self.system_prompt = system_prompt
        self.verbose = verbose
        self.response = None

    def send(self):
        start_time = time.time()
        try:
            self.response = self.client.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": self.prompt},
                ],
            )
        except Exception as e:
            print(f"An error occurred while sending the prompt: {e}")
            self.response = None
        end_time = time.time()

        if self.verbose:
            self._print_verbose_output(start_time, end_time)

        return self.response.choices[0].message.content if self.response.choices else "No response"

    def _print_verbose_output(self, start_time, end_time):
        elapsed_time = end_time - start_time
        token_count = self._get_token_count()

        input_tokens, output_tokens, total_tokens = self._get_token_details()
        cost = self._calculate_cost(input_tokens, output_tokens)

        print("Response:", self.response.choices[0].message.content)
        print("Tokens used:", token_count)
        print(f"Time elapsed: {elapsed_time:.2f} seconds")
        print(f"Estimated Cost: ${cost}")

    def _get_token_count(self):
        if hasattr(self.response, 'usage') and hasattr(self.response.usage, 'total_tokens'):
            return self.response.usage.total_tokens
        return "Token count not available"

    def _get_token_details(self):
        if hasattr(self.response, 'usage'):
            input_tokens = self.response.usage.prompt_tokens
            output_tokens = self.response.usage.completion_tokens
            total_tokens = input_tokens + output_tokens
            return input_tokens, output_tokens, total_tokens
        return "Unavailable", "Unavailable", "Unavailable"

    def _calculate_cost(self, input_tokens, output_tokens):
        input_token_cost = 0.0005 / 1000  # Cost per input token
        output_token_cost = 0.0015 / 1000  # Cost per output token
        if isinstance(input_tokens, int) and isinstance(output_tokens, int):
            return round((input_tokens * input_token_cost) + (output_tokens * output_token_cost), 5)
        return "Cost calculation not available"