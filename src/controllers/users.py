from typing import Dict
from ..view.user import user_view
from ..models.user import user_model
class user_controller(user_view,user_model):
    def __init__(self) -> None:
        super().__init__()
        pass
    
    
    def user_login(self,data_user:Dict):
        try:
            data_frame = self.read_uniq({'email' : str(data_user['email'])})

            if data_frame.empty:
                print("Email tidak ditemukan.")
                return
            
            email , password = str(data_frame['email'][0]), str(data_frame['password'][0])
            
            if email == str(data_user['email']):
                if password == str(data_user['password']):
                    print('Berhasil login')
                    return True
                else:
                    print('Password salah.')
                    return False
            else:
                print('Email salah.')
                return False
                
        except ValueError :
            print('Email salah') 
            return False
    
    def user_register(self,data_user:Dict):
        '''
        validasi data user
        '''
        user = self.read_uniq({'email' : data_user['email']})
        
        if len(user) > 0 :
            print('Email sudah di gunakan.')
            return False
        
        add_data = self.create_user(data_user)
        response = self.view_register_user(add_data)
        if response['status'] == 201:
            return True
        else :
            return False