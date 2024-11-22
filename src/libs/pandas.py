from pandas import  concat,DataFrame, read_json
from typing import Dict, Optional


class PandasHandler:
    def __init__(
        self, 
        path:str
        ) -> None:
        self.PATH = path
        pass

    def load(
        self,
        ) -> DataFrame:
        
        return read_json(self.PATH)

    def save(
        self, 
        data: DataFrame
        ) -> None:
        """
        Menyimpan DataFrame ke file JSON.
        """
        data.to_json(self.PATH, orient="records", indent=4)

    def create(
        self, 
        data: Dict
        ) -> DataFrame:
        """
        Menambahkan data baru ke DataFrame.
        """
        
        datas = self.load()
        new_data = DataFrame(data)
        
        datas = concat([datas, new_data], ignore_index=True) 

        self.save(datas)
        return datas

    def read(
        self,
        path : Optional[str] = None
        ) -> DataFrame:
        """
        Membaca seluruh data dari file JSON.
        """
        if not path :
            return self.load()
        else :
            return read_json(path)

    def read_uniq(
        self,
        where:Dict
        )-> DataFrame:
        """
        Membaca data dari file JSON berdasarkan key.
        """
        datas = DataFrame(self.load()) 
        column_name = list(where.keys())[0]
        filter_value = where[column_name] 
        return datas[datas[column_name] == filter_value] 
        
    
    def update(
        self, 
        id: int, 
        data_new: Dict
        ) -> DataFrame:
        """
        Memperbarui baris dengan ID tertentu di DataFrame.
        """
        datas = self.load()
        if id < 0 or id >= len(datas):
            raise IndexError("ID tidak valid.")
        datas.loc[id] = data_new
        self.save(datas)
        return datas

    def delete(
        self, 
        id: int
        ) -> DataFrame:
        """
        Menghapus baris dengan ID tertentu dari DataFrame.
        """
        datas = self.load()
        if id < 0 or id >= len(datas):
            raise IndexError("ID tidak valid.")
        datas = datas.drop(index=id).reset_index(drop=True)
        self.save(datas)
        return datas

