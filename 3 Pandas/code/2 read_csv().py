# read_csv() metodu, CSV formatinda olan fayllari oxumaq ucun istifade edilir.

# Birden cox parametr qebul ede bilir. Ancaq bunlari lazim olduqca istifade etdikde
# internetden girib goturmek daha mentiqlidir.



import pandas as pd


df = pd.read_csv('Datasets-main/company.csv')
print(df)