import os
from ..libs.pandas import PandasHandler

class cart_model(PandasHandler) :
    def __init__(self) -> None:
        self.PATH = os.path.join(os.getcwd(), 'src', 'data', 'users.json')
        super().__init__(self.PATH)
        pass
    
    def create_cart(self, data):
        return self.create(data)