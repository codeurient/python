# isnull() - funksiyasi verilənlər bazasindaki hər bir dəyərin null (NULL və ya NaN) olub olmadığını yoxlayır. 
# Bu funksiya hər bir dəyər üçün "True" (Bos deyerler True) və ya "False" (Dolu deyerler False) qaytarır.

import pandas as pd

melumatlar = pd.read_excel('Datasets-main/ESD.xlsx')

print(melumatlar)
print(melumatlar.isnull().sum())    # 915 bos deyer var 