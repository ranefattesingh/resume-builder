from constants.experience import TECH_STACK, TITLE
from constants.project import IS_TEAM_PROJECT, MOTIVATION, MY_ROLE, OTHER_COLLABORATORS, PROJECT_DESCRIPTION
from models.project import Project


class ProjectBuilder:
    _title                  = ''
    _description            = []
    _motivation             = ''
    _tech_stack             = []
    _other_collaborators    = []
    _my_role                = ''
    _is_team_project        = False

    _input_json    : dict

    def __init__(self, data: dict) -> None:
        self._input_json = data

    def add_title(self):
        if self._input_json.get(TITLE) is None:
            return self
        
        self._title = self._input_json[TITLE]

        return self
    
    def add_description(self):
        if self._input_json.get(PROJECT_DESCRIPTION) is None:
            return self
        
        if type(self._input_json[PROJECT_DESCRIPTION]) is not list:
            return self
        
        self._description = self._input_json[PROJECT_DESCRIPTION]

        return self
    
    def add_motivation(self):
        if self._input_json.get(MOTIVATION) is None:
            return self
        
        self._motivation = self._input_json[MOTIVATION]

        return self
    
    def add_tech_stack(self):
        if self._input_json.get(TECH_STACK) is None:
            return self
        
        if type(self._input_json[TECH_STACK]) is not list:
            return self
        
        self._tech_stack = self._input_json[TECH_STACK]

        return self
    
    
    def add_my_role(self):
        if self._input_json.get(MY_ROLE) is None:
            return self
        
        self._my_role = self._input_json[MY_ROLE]

        return self
    
    def add_other_collaborators(self):
        if self._input_json.get(OTHER_COLLABORATORS) is None:
            return self
        
        if type(self._input_json[OTHER_COLLABORATORS]) is not list:
            return self
        
        self._other_collaborators = self._input_json[OTHER_COLLABORATORS]

        return self
    
    def add_is_team_project(self):
        if self._input_json.get(IS_TEAM_PROJECT) is None:
            return self
        
        self._is_team_project = self._input_json[IS_TEAM_PROJECT]

        return self
    
    def build(self):
        return Project(self._title, self._description, self._motivation, self._tech_stack, self._other_collaborators, self._my_role, self._is_team_project)