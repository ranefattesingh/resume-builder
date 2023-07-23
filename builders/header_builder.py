from constants.header import DETAILS, FIELD_ICON, FIELD_TYPE, FIELD_VALUE, INTRODUCTION, NAME
from models.detail import Detail
from models.header import Header


class HeaderBuilder:
    _name    : str
    _details = []
    _intro   : str

    _input_json    : dict

    def __init__(self, data: dict) -> None:
        self._name    = ''
        self._details = []
        self._intro   = ''
        self._input_json = data

    def add_name(self):
        if self._input_json.get(NAME) is None:
            return self
        
        self._name = self._input_json[NAME]

        return self
    
    def add_details(self):
        if self._input_json.get(DETAILS) is None:
            return self
        
        details_array = self._input_json[DETAILS]
        if type(details_array) is not list:
            return self
        
        for detail in details_array:
            if type(detail) is not dict:
                return self
            
            self._details.append(self._get_detail(detail))

        return self
    
    def _get_detail(self, detail_json: dict) -> Detail:
        detail_fields = detail_json.keys()

        detail = Detail()
        for detail_field in detail_fields:
            if detail_field == FIELD_ICON:
                detail.field_icon = detail_json[FIELD_ICON]
            elif detail_field == FIELD_TYPE:
                detail.field_type = detail_json[FIELD_TYPE]
            else:
                detail.field_value = detail_json[FIELD_VALUE]
            
        return detail
    
    def add_introduction(self):
        if self._input_json.get(INTRODUCTION) is None:
            return self
        
        self._intro = self._input_json[INTRODUCTION]

        return self
    
    def build(self):
        return Header(self._name, self._details, self._intro)