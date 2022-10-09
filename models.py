from dataclasses_json import dataclass_json, config
from dataclasses import dataclass, field
from phpserialize import unserialize
import re

@dataclass_json
@dataclass
class Template_data:
    text: str    


@dataclass_json
@dataclass
class Assignment_content:
    template_data: str = field(metadata=config(field_name='templateData'))
    
    @property
    def data(self):
        data = bytes(self.template_data, encoding='utf-8')
        return unserialize(data)
    
    @property
    def answer_value(self):
        _data  = self.data[b'text'].decode('utf-8')
        _response = self.data[b'respons']
        if "lucktext" in _data or 'input' in _data:
            re_all = re.compile(r"(?:\[\w+])([^\[]+)\[[\/\\]\w+]")
            return(re_all.findall(_data))

        try:
            try:
                return [_response[0][b'value'][0].decode("utf-8")]
            except:
                return [_response[0][b'value'].decode("utf-8")]
        except:
            try:
                return [_response[b"'0'"][b'value'][0].decode("utf-8")] 
            except:
                return  [_response[b"'0'"][b'value'].decode("utf-8")]
    
    
@dataclass_json
@dataclass
class Assignment:
    assignment_id: int = field(metadata=config(field_name="assignmentID"))
    template_data : Template_data
    content: Assignment_content = field(metadata=config(field_name='assignment_content'))

