# pip install openpyxl

# openpyxl Python kitabxanasidir ve Excel (xlsx) faylları ilə işləmək imkanlarını təmin edir.

# read_excel()  metodu, xlsx formatinda olan fayllari oxumaq ucun istifade edilir.

import pandas as pd

df = pd.read_excel('Datasets-main/expense3.xlsx')
print(df)