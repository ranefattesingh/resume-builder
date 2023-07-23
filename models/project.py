class Project:
    title               : str
    description         : list
    motivation          : str
    tech_stack          : list
    other_collaborators : list
    my_role             : list
    is_team_project     : bool

    def __init__(self, title:str, descriptipn: list, motivation: str, tech_stack: list, other_collaborators: list, my_role: str, is_team_project: bool) -> None:
        self.title = title
        self.description = descriptipn
        self.motivation = motivation
        self.tech_stack = tech_stack
        self.other_collaborators = other_collaborators
        self.my_role = my_role
        self.is_team_project = is_team_project