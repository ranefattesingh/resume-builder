class Achievement:
    name       : str
    description : list
    when        : str

    def __init__(self, name: str, description: list, when: str) -> None:
        self.name           = name
        self.description    = description
        self.when           = when