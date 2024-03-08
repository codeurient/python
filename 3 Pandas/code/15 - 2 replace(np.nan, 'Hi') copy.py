# replace() - funksiyası DataFrame-də müəyyən dəyərləri başqa bir dəyərlə əvəz etmək üçün istifadə olunur.


import pandas as pd
import numpy as np

melumatlar = pd.read_csv('Datasets-main/company1.csv')

# Ilk once cedveldeki 'salary' sutununu cagirirq ki, hemin sutuna beraberlik = simvolu ile gonderek. Neyi ?
# Yeniden hemin sutuna muraciet ederek replace() funksiyasi ile, boslugu evez etdiyimiz 30000 deyeri ile.
melumatlar['salary'] = melumatlar['salary'].replace(np.nan, 30000)

print(melumatlar) 