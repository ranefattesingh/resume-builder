from builders.header_builder import HeaderBuilder
from constants.header import HEADER
from models.header import Header
from models.resume import Resume


class ResumeBuilder:
    _header          : Header
    _educations      : list
    _internships     : list
    _work_experiences: list
    _projects        : list
    _skillset        : list
    _achievements    : list
    _hobbies         : list
    _languages       : list
    _input_json      : dict

    def __init__(self, data: dict):
        self._input_json = data

    def add_header(self):
        if self._input_json.get(HEADER) is None:
            return self

        self._header = HeaderBuilder(self._input_json[HEADER]).add_name().add_details().add_introduction().build()

        return self
    
    def build(self):
        return Resume(self._header)