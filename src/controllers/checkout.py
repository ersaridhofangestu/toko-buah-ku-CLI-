from ..utils.selection import select
from ..models.checkout import checkout_modul

class checkout_controller(checkout_modul) :
    def __init__(self) -> None:
        super().__init__()
        pass
    
    def validation_checkout(self,pyment, data):
        if pyment.split(' ')[-1] == 'Cash':
            price = int(data.loc[0, 'total_price'])
            method = select(
                        type='input',
                        name='cash',
                        validate=lambda val: (val.isdigit() and int(val) >= price ) or 'Masukan nominal uang dan pastikan cukup untuk membayar' ,
                        message='bayar ? ',
                    )
            money = int(method['cash'])
            print(f'Anda membayar sebesar Rp. {money:,.0f}')
                            
            if money > price :
                print(f'Uang kembalian anda sebesar Rp. {(money - price):,.0f}')
            else:    
                print('Uang anda pas')
                                
        else:
            print('Pesanan anda segera di kirim ke alamat anda.') 
            print('Pesanan anda berhasil di buat')
        print('Trimakasih sudah memesan di toko buah ku')
        data['status'] = 'success'
        self.checkin(data=data)
        return