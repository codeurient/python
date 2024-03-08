import pandas as pd

melumatlar = pd.read_csv('Datasets-main/company1.csv')

print(melumatlar)    
print(melumatlar.duplicated())    

# duplicated() funksiyasinin onunde sum() funksiyasini yazaraq tekrarlnan setrlerin
# sayisini elde etmek mumkundur.
print(melumatlar['EEID'].duplicated().sum())    