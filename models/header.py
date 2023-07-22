class Header:
    name    : str
    details : list
    intro   : str

    def __init__(self, name, details, intro) -> None:
        self.name = name
        self.details = details
        self.intro = intro