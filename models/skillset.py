class Skillset:
    skill_name      : str
    description     : list

    def __init__(self, skillset_name : str, skillset_description : list) -> None:
        self.skill_name = skillset_name
        self.description = skillset_description