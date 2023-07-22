from models.detail import Detail


class Header:
    name    : str
    details : list
    intro   : str

    def __init__(self, name : str, details : Detail, intro : str) -> None:
        self.name = name
        self.details = details
        self.intro = intro