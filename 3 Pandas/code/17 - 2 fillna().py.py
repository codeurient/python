import pandas as pd

melumatlar = pd.read_csv('Datasets-main/company1.csv')

# Bir basa string teyin ederek bos xanalari bu deyer ile de doldur deye bilirik.
print(melumatlar.fillna('Hello')) 