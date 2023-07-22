from constants.experience import DESCRIPTION, LOCATION, ORGANIZATION, TECH_STACK, TITLE
from models.duration import Duration
from models.experience import Experience
from utils.utils import get_duration


class ExperienceBuilder:
    _title                  = ''
    _organization           = ''
    _branch                 = ''
    _location               = ''
    _experience_duration    = Duration()
    _description            = []
    _tech_stack             = []

    _input_json    : dict

    def __init__(self, data: dict) -> None:
        self._input_json = data

    def add_title(self):
        if self._input_json.get(TITLE) is None:
            return self
        
        self._title = self._input_json[TITLE]

        return self
    
    def add_organization(self):
        if self._input_json.get(ORGANIZATION) is None:
            return self
        
        self._organization = self._input_json[ORGANIZATION]

        return self
    
    def add_location(self):
        if self._input_json.get(LOCATION) is None:
            return self
        
        self._location = self._input_json[LOCATION]

        return self
    
    def add_description(self):
        if self._input_json.get(DESCRIPTION) is None:
            return self
        
        if type(self._input_json[DESCRIPTION]) is not list:
            return self
        
        self._description = self._input_json[DESCRIPTION]

        return self
    
    def add_tech_stack(self):
        if self._input_json.get(TECH_STACK) is None:
            return self
        
        if type(self._input_json[TECH_STACK]) is not list:
            return self
        
        self._tech_stack = self._input_json[TECH_STACK]

        return self
    
    
    def add_experience_duration(self, key: str):
        if self._input_json.get(key) is None:
            return self
        
        experience_duration = self._input_json[key]
        if type(experience_duration) is not dict:
            return self
        
        self._experience_duration = get_duration(experience_duration)

        return self
    
    
    def build(self):
        return Experience(self._title, self._organization, self._location, self._description, self._tech_stack, self._experience_duration)