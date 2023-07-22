from constants.achievement import ACHIEVEMENT_DESCRIPTION, ACHIEVEMENT_NAME, ACHIEVEMENT_WHEN
from models.achievement import Achievement


class AchievementBuilder:
    _achievement_name   = ''
    _description        = []
    _when               = ''

    input_json : dict

    def __init__(self, input_json: dict) -> None:
        self.input_json = input_json

    def add_name(self):
       if self.input_json.get(ACHIEVEMENT_NAME) is None:
           return self
       
       self._achievement_name = self.input_json[ACHIEVEMENT_NAME]

       return self
    
    def add_description(self):
        if self.input_json.get(ACHIEVEMENT_DESCRIPTION) is None:
            return self
        
        if type(self.input_json[ACHIEVEMENT_DESCRIPTION]) is not list:
            return self
        
        self._description = self.input_json[ACHIEVEMENT_DESCRIPTION]

        return self

    def add_when(self):
       if self.input_json.get(ACHIEVEMENT_WHEN) is None:
           return self
       
       self._when = self.input_json[ACHIEVEMENT_WHEN]

       return self
    
    def build(self):
        return Achievement(self._achievement_name, self._description, self._when)