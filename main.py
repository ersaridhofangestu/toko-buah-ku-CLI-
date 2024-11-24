from src.utils.selection import select
from src.controllers.users import user_controller
from src.controllers.cart import cart_controller
from src.controllers.checkout import checkout_controller

import os
from rich.console import Console
from time import sleep
from tabulate import tabulate
from pandas import DataFrame,read_json


if __name__ == '__main__':

    user_config = user_controller()
    cart_config = cart_controller()
    checkout = checkout_controller()
    
    email = None
    
    title = ' selamt datang di toko buah ku '.upper()
    len_char = len(title) + 10
    icon = '='
    print(f'''
    {icon*len_char}
    {title.center(len_char,icon)}
    {icon*len_char}
          ''')

    sleep(2)

    answers:str = select(type='list',name='home-menu',choices=['\uF08b  Login','\uF234  Register','\uF011  Exit'], message="pilih opsi")
    
    if not answers['home-menu'].split(' ')[-1] == 'Exit':
        if answers['home-menu'].split(' ')[-1]== 'Login':
            
            while True :
                sleep(0.5)
                email = select(
                                    type='input',
                                    name='email', 
                                    message="silakan masukan email :",
                                    validate=lambda val: 'Harap masukkan email yang valid' if '@' not in val or '.' not in val else True)
                sleep(0.5)
                password = select(
                                    type='password',
                                    name='password', 
                                    message="silakan masukan password :")
                                    
                new_data_user = {
                                'email': email['email'],
                                'password': str(password['password'])
                }

                
                # dummy = {'email':'ersa@gmail.com','password':'9090'}
                status_user = user_config.user_login(data_user=new_data_user)
                        
                if status_user == True :
                    break
                else :
                    continue
        if answers['home-menu'].split(' ')[-1] == 'Register':
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
                            break
                        else :
                            continue
        
        sleep(3)
        while True :
            Console().clear()
        
            title = ' menu pelanggan '.upper()
            print(f'''
        {icon*len_char}
        {title.center(len_char,icon)}
        {icon*len_char}
            ''')
            sleep(2)
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
                    Console().clear()
                    title = ' fresh fruit '.upper()
                    print(f'''
        {icon*len_char}
        {title.center(len_char,icon)}
        {icon*len_char}
            ''')  
                    path_file_menu = os.path.join(os.getcwd(), 'src', 'data', 'products.json')
                    menu = read_json(path_file_menu)
                    sleep(0.5)
                    tabel_menu = tabulate(DataFrame(menu), headers='keys',tablefmt='grid',showindex=False)
                    print(tabel_menu)
                    while True :
                        sleep(3)
                        answers:str = select(type='confirm',name='pelanggan-menu-menu', message="Keluar")
                        if answers['pelanggan-menu-menu']:
                            break
                        else:
                            continue
                case 'Cart':
                    Console().clear()
                    title = ' shopping card '.upper()
                    print(f'''
        {icon*len_char}
        {title.center(len_char,icon)}
        {icon*len_char}
            ''')  
                    sleep(0.5)
                    cart_new = cart_config.create_cart_validation(email['email'])

                    
                case 'Checkout':
                    
                    cart = cart_config.read_cart(where=email).reset_index(drop=True)

                    if cart.empty :
                        sleep(1)
                        print('\uF129 Anda tidak bisa checkout karna cart belom di buat.')
                        sleep(3)
                        continue
                    
                    title = ' checkout '.upper()
                    Console().clear()
                    print(f'''
        {icon*len_char}
        {title.center(len_char,icon)}
        {icon*len_char}
            ''')  
                    sleep(0.5)
                    print(f'''
ID pesanan {cart.loc[0, 'id']}
Email pemesan {cart.loc[0, 'email']}
Pesanan anda :
{tabulate(DataFrame(cart.loc[0, 'items']), headers='keys',tablefmt='grid',showindex=False)}
Total harga Rp. {cart.loc[0, 'total_price']:,.0f}
                          ''')
                    
                    sleep(0.5)
                    confirm = select(
                        type='confirm',
                        name='continue',
                        message='Apakah anda ingin checkout sekarang ?',
                    )
                    
                    if not confirm['continue']:
                        continue
                    
                    sleep(0.5)
                    address = select(
                        type='input',
                        name='location',
                        validate=lambda val: len(val) >= 25 or 'Harus detail minimal 25 karakter!' ,
                        message='Masukan alamat anda dengan details ?',
                    )
                    
                    sleep(0.5)
                    payment = select(
                        type='list',
                        name='method',
                        choices=[
                            '\uF0d6  Cash',
                            '\uF0d1  Cash-on-Delivery',
                            '\uF09d  Credit-Cart'
                            ], 
                        message="Pilih buah yang ingin dibeli"
                    )
                    
                    cart['address'] = address['location']
                    cart['payment'] = payment['method'].split(' ')[-1]

                    sleep(0.5)
                    checkout.validation_checkout(pyment=payment['method'],data=cart)

                    cart_config.delete_cart(cart.loc[0,'id'])
                
                    sleep(3)
                    Console().clear()
                    
                case 'Logout':
                    Console().clear()
                    exit()
    else:
        exit()