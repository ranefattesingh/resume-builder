from constants.duration import DURATION, FROM, TO
from models.duration import Duration


def get_duration(course_duration: dict) -> Duration:
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