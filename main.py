from src.utils.selection import select
from src.controllers.users import user_controller
import os
from pandas import DataFrame

if __name__ == '__main__':

    user_config = user_controller()
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
                # email = select(
                #                     type='input',
                #                     name='email', 
                #                     message="silakan masukan email",
                #                     validate=lambda val: 'Harap masukkan email yang valid' if '@' not in val or '.' not in val else True)
                # password = select(
                #                     type='password',
                #                     name='password', 
                #                     message="silakan masukan password")
                                    
                # new_data_user = {
                #                 'email': email['email'],
                #                 'password': str(password['password'])
                # }

                
                            
                status_user = user_config.user_login(data_user={'email':'ersa@gmail.com','password':'9090'})
                        
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

                customer_selection = { 
                    "email": email,
                    "items": [], 
                    "total_price": 0 
                }

                item_prices = []

                '''
                Memuat data produk dari file JSON
                '''
                path_to_products_file = os.path.join(os.getcwd(), 'src', 'data', 'products.json')
                product_list = user_config.load(path_to_products_file)

                '''
                Memformat data produk untuk ditampilkan
                '''
                product_list['formatted'] = product_list.apply(
                    lambda row: f'{row["id"]}) {row["name"]}/{row["unit"]} - Rp. {row["price"]:,.0f}', 
                    axis=1
                ).reset_index(drop=True)

                '''
                Proses memilih produk yang ingin dibeli pelanggan
                '''
                
                while True:
                    
                    selected_product_answer = select(
                        type='list',
                        name='selected_option',
                        choices=product_list['formatted'], 
                        message="Pilih buah yang ingin dibeli"
                    )
                    
                    selected_option_id = selected_product_answer['selected_option'].split(')')[0]
                    
                    selected_product = product_list[product_list['id'] == int(selected_option_id)].reset_index(drop=True)
                    
                    purchase_quantity = int(input(
                        f'Anda ingin membeli {selected_product.loc[0, "name"]} berapa {selected_product.loc[0, "unit"]} ? '
                    ))
                    
                    purchased_item = {
                        "name": selected_product.loc[0, "name"],
                        "price": int(selected_product.loc[0, "price"]),
                        'quantity': purchase_quantity,
                        "total": int(selected_product.loc[0, "price"]) * purchase_quantity
                    }
                    
                    item_prices.append(purchased_item['total'])
                    
                    customer_selection['items'].append(purchased_item)

                    continue_answer = select(
                        type='confirm',
                        name='continue_shopping',
                        message="Keluar dari menu pembelian?"
                    )
                    if continue_answer['continue_shopping']:
                        break

                '''
                Fungsi rekursif untuk menghitung total harga pembelian
                '''
                def calculate_total(prices: list):
                    if len(prices) == 0:
                        return 0
                    
                    return prices[0] + calculate_total(prices[1:])

                customer_selection['total_price'] = calculate_total(item_prices)

                print(customer_selection)

            case 'Checkout':
                print('checkout')
            case 'Logout':
                exit()
    else:
        exit()