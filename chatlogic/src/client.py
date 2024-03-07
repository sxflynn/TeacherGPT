from openai import OpenAI, AsyncOpenAI
from src.config import Config

class LLMClient:
    def __init__(self, config = None, async_client = False):
        self.config = config if config else Config()
        self.client = self._get_client(async_client)
    
    def _get_client(self, async_client):
        if async_client:
            return AsyncOpenAI(
                api_key=self.config.key,
                base_url=self.config.url
            )
        return OpenAI(
                api_key=self.config.key,
                base_url=self.config.url
            )
    
    
    # unused code below
    # async def send_prompt_async(self, prompt, system_prompt):
    #     if self.async_client:
    #         return await self.client.chat.completions.create(
    #             model=self.model,
    #             messages=[
    #                 {"role": "system", "content": system_prompt},
    #                 {"role": "user", "content": prompt},
    #             ],
    #         )
    #     else:
    #         raise NotImplementedError("Client has been initialized without async. Use send_prompt instead.")

    # def send_prompt(self, prompt, system_prompt):
    #     if not self.async_client:
    #         return self.client.chat.completions.create(
    #             model=self.model,
    #             messages=[
    #                 {"role": "system", "content": system_prompt},
    #                 {"role": "user", "content": prompt},
    #             ],
    #         )
    #     else:
    #         raise NotImplementedError("Client has been initialized as Async. Use send_prompt_async instead.")