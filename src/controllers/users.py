from ..view.user import user_view
from ..models.user import user_model

from typing import Dict
from time import sleep

class user_controller(user_view,user_model):
    def __init__(self) -> None:
        super().__init__()
        pass
    
    
    def user_login(self,data_user:Dict):
        try:
            data_frame = self.read_uniq(where={'email' : str(data_user['email'])}).reset_index(drop=True)
            if data_frame.empty:
                print("Email tidak ditemukan.")
                return
            
            email , password = str(data_frame.loc[0,'email']), str(data_frame.loc[0,'password'])
            
            if email == str(data_user['email']):
                if password == str(data_user['password']):
                    sleep(0.5)
                    print('\uF00c  Berhasil login')
                    return True
                else:
                    print('\uF00d  Password salah.')
                    return False
            else:
                sleep(2)
                print('\uF00d  Email salah.')
                return False
                
        except ValueError :
            sleep(2)
            print('\uF00d  Email salah') 
            return False
    
    def user_register(self,data_user:Dict):
        
        user = self.read_uniq(where={'email' : data_user['email']})
        
        if len(user) > 0 :
            sleep(0.5)
            print('\uF00d  Email sudah di gunakan.')
            return False
        
        add_data = self.create_user(data=data_user)
        response = self.view_register_user(add_data)
        if response['status'] == 201:
            return True
        else :
            return False