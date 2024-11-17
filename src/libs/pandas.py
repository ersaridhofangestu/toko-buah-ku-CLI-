from pandas import concat,DataFrame,read_json
from typing import Dict,List

class pandas :
    def __init__(self,path) -> None:
        self.PATH = path
        pass
    
    def load(self):
        return read_json(self.PATH)
    
    def save(self,data:DataFrame):
        data.to_json(self.PATH, orient="records", lines=True)
    
    def create(self, data:List[Dict]):
        datas = self.load()
        new_data = DataFrame(data)
        datas = concat([datas, new_data],ignore_index=True)
        self.save(datas)