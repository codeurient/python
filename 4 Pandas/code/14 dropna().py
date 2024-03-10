# drop_duplicates() - funksiyası DataFrame-dən eksik (NaN) dəyərləri olan sətirləri silmək üçün istifadə olunur.



import pandas as pd

melumatlar = pd.read_csv('Datasets-main/company1.csv')

# 2cisi ise yene EEID sutununda tekrarlanan setri silerek cedvelin ozunu qaytarir. 
print(melumatlar) 
print('*****************************************************************')
print('*****************************************************************')
print(melumatlar.dropna()) 