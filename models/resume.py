from models.header import Header


class Resume:
    header          : Header
    educations      : list
    internships     : list
    work_experiences: list
    projects        : list
    skillset        : list
    achievements    : list
    hobbies         : list
    languages       : list

    def __init__(self, header: Header) -> None:
        self.header = header

