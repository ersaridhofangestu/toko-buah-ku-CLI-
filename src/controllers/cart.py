from ..models.cart import cart_model
from src.utils.selection import select
from src.models.product import prodcut_model
import os
from pandas import DataFrame


class cart_controller(cart_model):
    def __init__(self) -> None:
        super().__init__()
        pass
    def create_cart_validation(self,email):
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
                product_list = self.read(path=path_to_products_file)
                
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
                    
                    
                    purchase_quantity = select(
                        type='input',
                        name='quantity',
                        validate=lambda val: (val.isdigit() and int(val) >= 0) or 'Harus berupa angka positif!' ,
                        message=f'Anda ingin membeli {selected_product.loc[0, "name"]} berapa {selected_product.loc[0, "unit"]}',
                    )
                    
                    purchased_item = {
                        "name": selected_product.loc[0, "name"],
                        "price": int(selected_product.loc[0, "price"]),
                        'quantity': int(purchase_quantity['quantity']),
                        "total": int(selected_product.loc[0, "price"]) * int(purchase_quantity['quantity'])
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

                self.create_cart(customer_selection)
                return customer_selection