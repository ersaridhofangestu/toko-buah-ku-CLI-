from ..libs.pandas import PandasHandler
from typing import Dict
import os



class user_model(PandasHandler):
    def __init__(self) -> None:
        self.PATH = os.path.join(os.getcwd(), 'src', 'data', 'users.json')
        super().__init__(self.PATH)
        pass
        
    def create_user(self,data:Dict):
        return self.create([data])
    
    def read_user(self):
        return self.read()