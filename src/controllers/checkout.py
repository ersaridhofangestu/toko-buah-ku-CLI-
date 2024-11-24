from ..utils.selection import select
from ..models.checkout import checkout_modul

from time import sleep

class checkout_controller(checkout_modul) :
    def __init__(self) -> None:
        super().__init__()
        pass
    
    def validation_checkout(self,pyment, data):
        if pyment.split(' ')[-1] == 'Cash':
            price = int(data.loc[0, 'total_price'])
            sleep(0.5)
            method = select(
                        type='input',
                        name='cash',
                        validate=lambda val: (val.isdigit() and int(val) >= price ) or 'Masukan nominal uang dan pastikan cukup untuk membayar' ,
                        message='bayar ? ',
                    )
            money = int(method['cash'])
            sleep(0.5)
            print(f'\uF129  Anda membayar sebesar Rp. {money:,.0f}')
                            
            if money > price :
                sleep(0.5)
                print(f'\uF129  Uang kembalian anda sebesar Rp. {(money - price):,.0f}')
            else:    
                sleep(0.5)
                print('\uF129  Uang anda pas')
                                
        else:
            sleep(0.5)
            print('\uF129  Pesanan anda segera di kirim ke alamat anda.') 
            print('\uF129  Pesanan anda berhasil di buat')
            sleep(0.5)
        print('\uF129  Trimakasih sudah memesan di toko buah ku')
        data['status'] = 'success'
        self.checkin(data=data)
        return