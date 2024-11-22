from ..libs.pandas import PandasHandler
import os

class prodcut_model(PandasHandler):
    def __init__(self) -> None:
        self.PATH= os.path.join(os.getcwd(), 'src', 'data', 'products.json')
        super().__init__(path=self.PATH)
        pass
        
    def get_products(self):
        print('list nya')
        # return self.load()