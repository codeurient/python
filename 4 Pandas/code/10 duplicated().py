# duplicated() - funksiyasi tekrarlanan sətirləri müəyyən etmək üçün istifadə olunur. Bu 
# funksiya eyni sətirlərin təkrar olub-olmadığını yoxlamaq üçün hər bir sətiri DataFrame-dəki digər 
# sətirlərlə müqayisə edir.

import pandas as pd

melumatlar = pd.read_csv('Datasets-main/company.csv')

print(melumatlar.duplicated())    


# Tekrarlanma varsa True
# Tekrarlanma yoxdursa False qayidir.