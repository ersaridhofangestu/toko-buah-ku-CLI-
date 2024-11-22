from ..libs.pandas import PandasHandler 
import os

class checkout_modul(PandasHandler):
    def __init__(self) -> None:
        self.PATH= os.path.join(os.getcwd(), 'src', 'data', 'checkout.json')
        super().__init__(path=self.PATH)
        pass
    
    def checkin(self,data):
        return self.create(data=data)