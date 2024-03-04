import json
from typing import List, Optional
from gql import gql, Client as GQLClient
from pydantic import BaseModel, ValidationError
from src.prompt import LLMPrompt, extractContent

prompt_mapping = {
    "student": "student_general_prompt",
    "attendance": "attendance_general_prompt",
}

class ApiDecision(BaseModel):
    api: str
    query: Optional[str] = None
    reason: Optional[str] = None
   
class Orchestrator:
    def __init__(self, gqlclient:GQLClient, user_prompt, prompts_file, system_prompt):
        self.gqlclient = gqlclient
        self.user_prompt = user_prompt
        self.prompts_file = prompts_file
        self.system_prompt = system_prompt
        self.collected_data = []
        
    def _get_orchestrator_prompt(self) -> str:
        return self.prompts_file.get('orchestrator_prompt').get('text')
      
    def _fetch_api_decision(self) -> str:
        api_decision_engine = LLMPrompt(
            prompt=(self._get_orchestrator_prompt() + self.user_prompt),
            system_prompt=self.system_prompt
            )
        return extractContent(api_decision_engine.send())  
        
    def prompt_for_apis(self) -> List[ApiDecision]:
        raw_decision_list = self._fetch_api_decision()
        try:
            decision_data = json.loads(raw_decision_list)  # Make sure to import json at the top
            validated_decision_list = [ApiDecision(**item) for item in decision_data]
            print("validated_decision_list is: ", validated_decision_list)
        except ValidationError as e:
            print("raw_decision_list couldn't validate: ", raw_decision_list)
            raise ValidationError(f"The AI failed to give a JSON object with fields and variables.: {e}") from e
        return validated_decision_list
            
            
        