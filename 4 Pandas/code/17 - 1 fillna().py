# fillna() - metodu çatışmayan dəyərləri doldurmaq üçün istifadə olunur. "bfill" (geri doldurma) parametri 
# ardıcıl olaraq çatışmayan dəyərləri, yəni NaN (boş) dəyərləri mövcud dəyərlərlə doldurur. Yəni NaN dəyəri 
# olan xanalar cedveldeki ondan sonra gelen xanadaki deyer ile doldurulur. 

# bfill - backward fill
# ffill - forward fill ve.s

import pandas as pd

melumatlar = pd.read_csv('Datasets-main/company1.csv')

print(melumatlar) 
print(melumatlar.fillna(method='bfill')) 