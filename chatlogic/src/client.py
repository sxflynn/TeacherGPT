from openai import OpenAI, AsyncOpenAI
from src.config import Config, settings

class LLMClient:
    def __init__(self, config = None, async_client = False, custom_service = settings.default_service):
        self.config = config if config else Config(custom_service)
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