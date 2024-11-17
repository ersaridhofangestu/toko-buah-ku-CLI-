from ..libs.pandas import pandas
from typing import Dict
import os


class user_model(pandas):
    def __init__(self) -> None:
        self.PATH = os.path.join(os.getcwd(), 'src', 'data', 'users.json')
        super().__init__(self.PATH)
        
    def create_user(self,data:Dict):
        return self.create([data])