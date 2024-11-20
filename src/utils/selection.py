from PyInquirer.prompt import prompt
from typing import Optional

def select(
    type:'input', 
    name:str ,
    choices: Optional[str] = None,
    default: Optional[bool] = None ,
    validate: Optional[str] = None,
    message:str = 'pilih opsi?'
    ) -> str | bool:
    questions = {
            'type': type,
            'name': name,
            'message':message.capitalize(),
        }
    
    
    if choices is not None :
        questions['choices'] = choices
    if default is not None :
        questions['default'] = default
    if validate is not None :
        questions['validate'] = validate
        
    
    answers = prompt([questions])
    
    return answers
