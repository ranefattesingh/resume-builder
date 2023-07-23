from constants.duration import DURATION, FROM, TO
from constants.education import COURSE_DURATION, DEGREE, INSTITUTE, SCORE, BRANCH
from models.duration import Duration
from models.education import Education


class EducationBuilder:
    _degree         : str
    _institute      : str
    _branch         : str
    _score          : str
    _course_duration : Duration

    _input_json    : dict

    def __init__(self, data: dict) -> None:
        self._input_json = data

    def add_degree(self):
        if self._input_json.get(DEGREE) is None:
            return self
        
        self._degree = self._input_json[DEGREE]

        return self
    
    def add_institute(self):
        if self._input_json.get(INSTITUTE) is None:
            return self
        
        self._institute = self._input_json[INSTITUTE]

        return self
    
    def add_branch(self):
        if self._input_json.get(BRANCH) is None:
            self._branch = ''

            return self
        
        self._branch = self._input_json[BRANCH]

        return self
    
    def add_score(self):
        if self._input_json.get(SCORE) is None:
            return self
        
        self._score = self._input_json[SCORE]

        return self
    
    def add_course_duration(self):
        if self._input_json.get(COURSE_DURATION) is None:
            return self
        
        course_dutaion = self._input_json[COURSE_DURATION]
        if type(course_dutaion) is not dict:
            return self
        
        self._course_duration = self._get_duration(course_dutaion)

        return self
    
    def _get_duration(self, course_duration: dict) -> Duration:
        course_duration_fields = course_duration.keys()

        duration = Duration()
        duration.duration = ''
        duration.from_date = ''
        duration.to_date = ''
        
        for course_duration_field in course_duration_fields:
            if course_duration_field == FROM:
                duration.from_date = course_duration[FROM]
            elif course_duration_field == TO:
                duration.to_date = course_duration[TO]
            elif course_duration_field == DURATION:
                duration.duration = course_duration[DURATION]
            
        return duration
    
    def build(self):
        return Education(self._degree, self._institute, self._branch, self._score, self._course_duration)