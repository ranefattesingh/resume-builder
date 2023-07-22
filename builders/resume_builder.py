from builders.education_builder import EducationBuilder
from builders.experience_builder import ExperienceBuilder
from builders.header_builder import HeaderBuilder
from constants.header import DETAILS
from constants.resume import EDUCATION, HEADER, INTERNSHIPS, WORK_EXPERIENCES
from models.detail import Detail
from models.header import Header
from models.resume import Resume


class ResumeBuilder:
    _header          = Header('', Detail(), '')
    _educations      = []
    _internships     = []
    _work_experiences= []
    _projects        = []
    _skillset        = []
    _achievements    = []
    _hobbies         = []
    _languages       = []

    _input_json      = dict()

    def __init__(self, data: dict) -> None:
        self._input_json = data

    def add_header(self):
        if self._input_json.get(HEADER) is None:
            return self

        self._header = HeaderBuilder(self._input_json[HEADER]).add_name().add_details().add_introduction().build()

        return self
    
    def add_educations(self):
        if self._input_json.get(EDUCATION) is None:
            return self
        
        education_array = self._input_json[EDUCATION]
        if type(education_array) is not list:
            return self

        for education in education_array:
            educationBuilder = EducationBuilder(education).add_degree().add_institute().add_branch().add_score().add_course_duration()
            self._educations.append(educationBuilder.build())

        return self
    
    def add_internships(self):
        if self._input_json.get(INTERNSHIPS) is None:
            return self
        
        internship_array = self._input_json[INTERNSHIPS]
        if type(internship_array) is not list:
            return self

        for internship in internship_array:
            internshipBuilder = ExperienceBuilder(internship).add_title().add_organization().add_description().add_experience_duration(INTERNSHIPS).add_location().add_tech_stack()
            self._internships.append(internshipBuilder.build())

        return self
    
    def add_work_experience(self):
        if self._input_json.get(WORK_EXPERIENCES) is None:
            return self
        
        work_experience_array = self._input_json[WORK_EXPERIENCES]
        if type(work_experience_array) is not list:
            return self

        for work_experience in work_experience_array:
            workExperienceBuilder = ExperienceBuilder(work_experience).add_title().add_organization().add_description().add_experience_duration(WORK_EXPERIENCES).add_location().add_tech_stack()
            self._work_experiences.append(workExperienceBuilder.build())

        return self
    
    def build(self):
        return Resume(self._header, self._educations, self._internships, self._work_experiences)