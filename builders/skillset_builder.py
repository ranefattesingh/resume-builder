from constants.skillset import SKILLSET_DESCRIPTION, SKILLSET_NAME
from models.skillset import Skillset


class SkillsetBuilder:
    _skillset_name = ''
    _skillset_description = []

    input_json : dict

    def __init__(self, input_json: dict) -> None:
        self.input_json = input_json

    def add_skillset_name(self):
       if self.input_json.get(SKILLSET_NAME) is None:
           return self
       
       self._skillset_name = self.input_json[SKILLSET_NAME]

       return self
    
    def add_skillset_description(self):
        if self.input_json.get(SKILLSET_DESCRIPTION) is None:
            return self
        
        if type(self.input_json[SKILLSET_DESCRIPTION]) is not list:
            return self
        
        self._skillset_description = self.input_json[SKILLSET_DESCRIPTION]

        return self
    
    def build(self):
        return Skillset(self._skillset_name, self._skillset_description)