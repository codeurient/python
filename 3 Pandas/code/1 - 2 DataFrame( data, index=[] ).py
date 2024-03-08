# loc() metoddan istifadə edərək, müəyyən bir şərtə uyğun gələn setrler üçün xüsusi sütunu yeniləyə bilərsiniz. Bununla belə, mövcud olmayan 
# sütunu yeniləməyə çalışsanız, həmin sütun avtomatik olaraq yaradılacaq və verilmiş dəyərlə doldurulacaq.

import pandas as pd

melumatlar = {  
                'Name':   ['Alice', 'Bob', 'Charlie', 'Dave'],
                'Age':    [25, 30, 35, 40],
                'Salary': [50000, 60000, 70000, 80000],
            }

# Varsayilan indeksler 0-dan baslayirdi. DataFrame() metodunun 2ci parametrinde varsayilan indeksleri 
# asagidaki formada yazaraq 'a', 'b', 'c', 'd' ve.s kimi indekslerle evez ede bilerik.
df = pd.DataFrame(melumatlar)  
print(df)

df = pd.DataFrame(melumatlar, index=['a', 'b', 'c', 'd'])  
print(df)