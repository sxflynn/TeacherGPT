from dotenv import load_dotenv
import tomllib, pathlib, os
from openai import OpenAI

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
    def __init__(self, provider_name):
        self.config_data = load_config()
        if not self.config_data.get(provider_name):
            raise ValueError(f"{provider_name} is not located in the config.toml file.")
        load_dotenv()
        provider = self.config_data.get(provider_name,{})
        self.url = provider.get('url','')
        self.key = os.getenv(f'{provider_name.upper()}_API_KEY', 'none') #OpenAI library requires key string
        self.models = provider.get('models', [])
        if not self.models:
            raise ValueError(f"No model selected for {provider_name}")
        self.selected_model = self.models[0]

    def set_model(self, model_name):
        if model_name in self.models:
            self.selected_model = model_name
        else:
            raise ValueError(f"Model {model_name} not found in configuration.")

class Template:
    _prompt_data = None
    
    @classmethod
    def _load_prompts(cls):
        if cls._prompt_data is None:
            cls._prompt_data = load_prompts()
    
    @classmethod
    def get_prompt_text(cls, section_name):
        cls._load_prompts()
        section = cls._prompt_data.get(section_name, {})
        return section.get('text', '')

class Client:
    def __init__(self, config: Config):
        self.client = OpenAI(
        api_key=config.key,
        base_url=config.url
        )
        self.model = config.selected_model
        
    def send_prompt(self, prompt, system_prompt):
        return self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
        )