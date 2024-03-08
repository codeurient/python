# mean() - funksiyasi reqemsal data-larin orta qiymətini hesablamaq üçün istifadə olunur.


import pandas as pd
import numpy as np

melumatlar = pd.read_csv('Datasets-main/company1.csv')

melumatlar['salary'] = melumatlar['salary'].replace(np.nan, 30000)

print(melumatlar) 
# ( 30 000 + 25 000 + 27 000 + 20 000 + 25 000 + 30 000 + 25 000 ) / 7 = 26000
print(melumatlar['salary'].mean()) 