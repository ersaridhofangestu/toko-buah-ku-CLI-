from src.utils.selection import select
from src.controllers.users import user_controller
from src.controllers.cart import cart_controller
from src.models.product import prodcut_model

import os
from pandas import DataFrame

if __name__ == '__main__':

    user_config = user_controller()
    cart_config = cart_controller()
    products = prodcut_model()
    
    email = None
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

                
                # dummy = {'email':'ersa@gmail.com','password':'9090'}
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
        
        while True :
        
            title = ' menu pelanggan '.upper()
            print(f'''
        {icon*len_char}
        {title.center(len_char,icon)}
        {icon*len_char}
            ''')
            answers:str = select(
                type='list',
                name='pelanggan-menu',
                choices=[
                    '\uF0ce  Menu',
                    '\uF07a  Cart',
                    '\uF09d  Checkout',
                    '\uF08b  Logout'], 
                message="pilih opsi")

            match answers['pelanggan-menu'].split(' ')[-1]:
                case 'Menu':
                    title = ' fresh fruit '.upper()
                    print(f'''
        {icon*len_char}
        {title.center(len_char,icon)}
        {icon*len_char}
            ''')  
                    path_file_menu = os.path.join(os.getcwd(), 'src', 'data', 'products.json')
                    menu = user_config.load(path_file_menu)
                    print(menu)

                    while True :
                        answers:str = select(type='confirm',name='pelanggan-menu-menu', message="Keluar")
                        if answers['pelanggan-menu-menu']:
                            break
                        else:
                            continue
                case 'Cart':
                    
                    title = ' shopping card '.upper()
                    print(f'''
        {icon*len_char}
        {title.center(len_char,icon)}
        {icon*len_char}
            ''')  
                    
                    cart_status = cart_config.create_cart_validation(email)

                    
                    print(cart_status)
                    
                case 'Checkout':
                    print('checkout')
                case 'Logout':
                    exit()
    else:
        exit()