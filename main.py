from src.utils.selection import select
from src.controllers.users import user_controller
import time

if __name__ == '__main__':

    user_config = user_controller()

    '''
        tampilan heading
    '''
    title = ' selamt datang di toko buah ku '.upper()
    len_char = len(title) + 10
    icon = '='
    print(f'''
    {icon*len_char}
    {title.center(len_char,icon)}
    {icon*len_char}
          ''')

    '''
        opsi di home menu
    '''
    answers:str = select(type='list',name='home-menu',choices=['Login','Register','Exit'], message="pilih opsi")
    
    '''
        if nested
    '''
    if not answers['home-menu'] == 'Exit':
        if answers['home-menu'] == 'Login':
            '''
                akses login
            '''
            while True :
                email = select(
                                    type='input',
                                    name='email', 
                                    message="silakan masukan email",
                                    validate=lambda val: 'Harap masukkan email yang valid' if '@' not in val or '.' not in val else True)
                password = select(
                                    type='password',
                                    name='password', 
                                    message="silakan masukan password")
                                    
                new_data_user = {
                                'email': email['email'],
                                'password': str(password['password'])
                }

                            
                            
                status_user = user_config.user_login(data_user=new_data_user)
                        
                if status_user == True :
                    print('testing')
                    break
                else :
                    continue
                
                
        if answers['home-menu'] == 'Register':
                while True :
                        '''
                            register
                        '''
                        email = select(
                                type='input',
                                name='email', 
                                message="silakan masukan email",
                                validate=lambda val: 'Harap masukkan email yang valid' if '@' not in val or '.' not in val else True)
                        password = select(
                                type='password',
                                name='password', 
                                message="silakan masukan password")
                                
                        new_data_user = {
                            'email': email['email'],
                            'password': str(password['password'])
                        }
                        
                        
                        status_user = user_config.user_register(data_user=new_data_user)
                        if status_user == True :
                            print('testing')
                            break
                        else :
                            continue
                        
        print('halo world')
        
    else:
        exit()