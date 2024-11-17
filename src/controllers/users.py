import click
from typing import Dict
from ..models.user import user_model

class user_controller(user_model):
    def __init__(self) -> None:
        super().__init__()
        pass
    
    
    def user_login(self,data_user:Dict):
        print({'data_user':data_user})
        return
    
    def user_register(self,data_user:Dict):
        self.create_user(data_user)
        return