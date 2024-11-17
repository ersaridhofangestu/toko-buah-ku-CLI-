from PyInquirer.prompt import prompt
from typing import Optional,List,Dict

def select(
    type:'input', 
    name:str ,
    choices: Optional[list[str]] = None,
    default: Optional[bool] = None ,
    validate: Optional[str] = None,
    message:str = 'pilih opsi?'
    ) -> Dict[str,str]:
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
        
    
    answers:Dict[str,str] = prompt([questions])
    
    return answers
