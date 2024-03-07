import tomllib, pathlib, os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    anyscale_api_key: str
    togetherai_api_key: str
    default_service: str
    graphql_url: str

settings = Settings()

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env') # Unnecesary when using Docker/cloud
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

def load_config():
    root_dir = pathlib.Path(__file__).parent.parent
    config_path = root_dir / 'config.toml'
    with config_path.open(mode="rb") as fp:
        config_data = tomllib.load(fp)
    return config_data

def load_prompts():
    root_dir = pathlib.Path(__file__).parent.parent
    prompt_path = root_dir / 'prompts.toml'
    with prompt_path.open(mode="rb") as fp:
        prompt_data = tomllib.load(fp)
    return prompt_data

class Config:
    def __init__(self, provider_name = settings.default_service):
        self.config_data = load_config()
        if not self.config_data.get(provider_name):
            raise ValueError(f"{provider_name} is not located in the config.toml file.")
        load_dotenv()
        provider = self.config_data.get(provider_name,{})
        self.url = provider.get('url','')
        self.key = os.getenv(f'{provider_name.upper()}_API_KEY', 'none') # OpenAI library requires key string
        self.models = provider.get('models', [])
        if not self.models:
            raise ValueError(f"No model selected for {provider_name}")
        self.selected_model = self.models[0]

    def set_model(self, model_name):
        if model_name in self.models:
            self.selected_model = model_name
        else:
            raise ValueError(f"Model {model_name} not found in configuration.")