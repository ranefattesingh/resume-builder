from builders.achievement_builder import AchievementBuilder
from builders.education_builder import EducationBuilder
from builders.experience_builder import ExperienceBuilder
from builders.header_builder import HeaderBuilder
from builders.project_builder import ProjectBuilder
from builders.skillset_builder import SkillsetBuilder
from constants.experience import WORK_DURAION, INTERNSHIP_DURAION
from constants.resume import ACHIEVEMENTS, EDUCATION, HEADER, HOBBIES, INTERESTS, INTERNSHIPS, LANGUAGES, PROJECTS, SKILLSET, WORK_EXPERIENCES
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
    _interests       = []
    _hobbies         = []
    _languages       = []

    _input_json      = dict()

    def __init__(self, data: dict) -> None:
        self._input_json = data
        self._header          = Header('', Detail(), '')
        self._educations      = []
        self._internships     = []
        self._work_experiences= []
        self._projects        = []
        self._skillset        = []
        self._achievements    = []
        self._interests       = []
        self._hobbies         = []
        self._languages       = []

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
            internshipBuilder = ExperienceBuilder(internship).add_title().add_organization().add_description().add_experience_duration(INTERNSHIP_DURAION).add_location().add_tech_stack()
            self._internships.append(internshipBuilder.build())

        return self
    
    def add_work_experience(self):
        if self._input_json.get(WORK_EXPERIENCES) is None:
            return self
        
        work_experience_array = self._input_json[WORK_EXPERIENCES]
        if type(work_experience_array) is not list:
            return self

        for work_experience in work_experience_array:
            workExperienceBuilder = ExperienceBuilder(work_experience).add_title().add_organization().add_description().add_experience_duration(WORK_DURAION).add_location().add_tech_stack()
            self._work_experiences.append(workExperienceBuilder.build())

        return self
    
    def add_projects(self):
        if self._input_json.get(PROJECTS) is None:
            return self
        
        projects_array = self._input_json[PROJECTS]
        if type(projects_array) is not list:
            return self

        for project in projects_array:
            projectBuilder = ProjectBuilder(project).add_title().add_description().add_tech_stack().add_other_collaborators().add_motivation().add_my_role().add_is_team_project()
            self._projects.append(projectBuilder.build())

        return self
    
    def add_skillset(self):
        if self._input_json.get(SKILLSET) is None:
            return self
        
        if type(self._input_json[SKILLSET]) is not list:
            return self
        
        for skill in self._input_json[SKILLSET]:
            skill_item = SkillsetBuilder(skill).add_skillset_name().add_skillset_description().build()
            self._skillset.append(skill_item)

        return self
    
    def add_achievements(self):
        if self._input_json.get(ACHIEVEMENTS) is None:
            return self
        
        if type(self._input_json[ACHIEVEMENTS]) is not list:
            return self
        
        for achievement in self._input_json[ACHIEVEMENTS]:
            achievement_item = AchievementBuilder(achievement).add_name().add_description().add_when().build()
            self._achievements.append(achievement_item)

        return self
    
    def add_interests(self):
        if self._input_json.get(INTERESTS) is None:
            return self
        
        if type(self._input_json[INTERESTS]) is not list:
            return self
        
        self._interests = self._input_json[INTERESTS]

        return self
    
    def add_hobbies(self):
        if self._input_json.get(HOBBIES) is None:
            return self
        
        if type(self._input_json[HOBBIES]) is not list:
            return self
        
        self._hobbies = self._input_json[HOBBIES]

        return self
    
    def add_languages(self):
        if self._input_json.get(LANGUAGES) is None:
            return self
        
        if type(self._input_json[LANGUAGES]) is not list:
            return self
        
        self._languages = self._input_json[LANGUAGES]

        return self

    
    def build(self):
        return Resume(self._header, self._educations, self._internships, self._work_experiences, self._projects, self._skillset, self._achievements, self._interests, self._hobbies, self._languages)