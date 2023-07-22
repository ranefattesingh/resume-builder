from models.detail import Detail
from models.header import Header


class Resume:
    header          = Header('', Detail(), '')
    educations      = []
    internships     = []
    work_experiences= []
    projects        = []
    skillset        = []
    achievements    = []
    hobbies         = []
    languages       = []

    def __init__(self, header: Header, educations: list, internships: list, work_experiences: list) -> None:
        self.header = header
        self.educations = educations
        self.internships = internships
        self.work_experiences = work_experiences

