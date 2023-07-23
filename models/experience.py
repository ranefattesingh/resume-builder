from models.duration import Duration


class Experience:
    organization: str
    title       : str
    location    : str
    description : list
    tech_stack  : list
    duration    : Duration

    def __init__(self, title: str, organization: str, location: str, description: list, tech_stack: list, duration: Duration) -> None:
        self.title          = title
        self.organization   = organization
        self.location       = location
        self.description    = description
        self.tech_stack     = tech_stack
        self.duration       = duration