from ..models.user import user_model
from typing import Dict
import os

class user_view(user_model):
    def __init__(self) -> None:
        super().__init__()
    
    def view_register_user(self,data:Dict):
        return {
                'status':201,
                'message':'Berhasil, data user sudah di buat.',
                'data' : data
            }