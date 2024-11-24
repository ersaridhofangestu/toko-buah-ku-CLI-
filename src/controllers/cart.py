from ..models.cart import cart_model
from src.utils.selection import select
import os
from pandas import DataFrame
from ..utils.character_random import random
from ..utils.calculate_total import calculate_total

class cart_controller(cart_model):
    def __init__(self) -> None:
        super().__init__()
        pass
    def create_cart_validation(self,email):
                path_to_products_file = os.path.join(os.getcwd(), 'src', 'data', 'products.json')
                product_list = self.read(path=path_to_products_file)

                customer_selection = { 
                    "id": random(10),
                    "email": email,
                    "items": [], 
                    "total_price": 0 
                }

                item_prices = []
                
                product_list['formatted'] = product_list.apply(
                    lambda row: f'{row["id"]}) {row["name"]}/{row["unit"]} - Rp. {row["price"]:,.0f}', 
                    axis=1
                ).reset_index(drop=True)
                
                def loop():
                    while True:
                    
                        selected_product_answer = select(
                            type='list',
                            name='selected_option',
                            choices=[*product_list['formatted'], 'Exit'], 
                            message="Pilih buah yang ingin dibeli"
                        )
                        
                        if selected_product_answer['selected_option'] == 'Exit':
                            return 'Exit'
                        
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
                        if "items" not in customer_selection or not isinstance(customer_selection["items"], list):
                            customer_selection["items"] = []
                        customer_selection['items'].append(purchased_item)

                        continue_answer = select(
                            type='confirm',
                            name='continue_shopping',
                            message="Lajut belanja ?"
                        )
                        if not continue_answer['continue_shopping']:
                            break
                        
                if loop() != 'Exit':
                    customer_selection['total_price'] = calculate_total(item_prices)
                    self.create_cart([customer_selection])
                    return customer_selection