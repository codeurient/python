import pandas as pd

melumatlar = pd.read_csv('Datasets-main/company1.csv')

print(melumatlar['EEID'].duplicated())