import pandas as pd

melumatlar = pd.read_csv('Datasets-main/company1.csv')

print(melumatlar)    
print(melumatlar.duplicated())    

# Istenilen her hansisa bir sutunu secmek de mumkundur. Bunun ucun ilk once [] kvadrat moterize
# qoyaraq sonra hemin sutunun adini string tipinde kvadrat moterize icinde yazmaq kifayetdir.
print(melumatlar['EEID'].duplicated())