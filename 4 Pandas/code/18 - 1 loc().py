# loc() metodundan istifadə edərək, müəyyən bir şərtə uyğun gələn sətrler üçün xüsusi sütunu əldə edə yaxud yeniləyə bilərsiniz. Bununla belə, 
# mövcud olmayan sütunu yeniləməyə çalışsanız, həmin sütun avtomatik olaraq yaradılacaq və verilmiş dəyərlə doldurulacaq.

import pandas as pd

melumatlar = {  
                'Name':   ['Alice', 'Bob', 'Charlie', 'Dave'],
                'Age':    [25, 30, 35, 40],
                'Salary': [50000, 60000, 70000, 80000],
            }

df1 = pd.DataFrame(melumatlar)  
#! 0-ci indeksde olan setire aid melumatlari elde etdik
secilen_setr1 = df1.loc[0]
print(secilen_setr1)


print('*************************************************************')


df2 = pd.DataFrame(melumatlar, index=['a', 'b', 'c', 'd'])  
#! b indeksinde olan setire aid melumatlari elde etdik
secilen_setr2 = df2.loc['b']
print(secilen_setr2)



















# melumatlar.loc[  melumatlar['Bonus %'] == 0, "GetBonus"  ] = "no bonus"
# melumatlar.loc[  melumatlar['Bonus %'] >  0, "GetBonus"  ] = "bonus"
# print(  melumatlar.head(10)  )


