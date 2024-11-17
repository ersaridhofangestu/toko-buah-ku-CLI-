from src.utils.selection import select
from src.controllers.users import user_controller

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
        
        '''
            login
        '''
        if answers['home-menu'] == 'Login':
            data_user = {
                'email':select(
                    type='input',
                    name='email', 
                    message="silakan masukan email",
                    validate=lambda val: 'Harap masukkan email yang valid' if '@' not in val or '.' not in val else True),
                'password':select(
                    type='password',
                    name='email', 
                    message="silakan masukan password")
            }
            
            req = user_config.user_login(data_user=data_user)
            
            
            
        '''
            register
        '''
        new_data_user = {
                'email':select(
                    type='input',
                    name='email', 
                    message="silakan masukan email",
                    validate=lambda val: 'Harap masukkan email yang valid' if '@' not in val or '.' not in val else True),
                'password':select(
                    type='password',
                    name='email', 
                    message="silakan masukan password")
            }
            
        req = user_config.user_register(data_user=new_data_user)
        
        
        if answers['home-menu'] == 'Register':
            print('register')
        
    else:
        exit()