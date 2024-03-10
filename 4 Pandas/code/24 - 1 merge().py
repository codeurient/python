# merge() funksiyası iki DataFrame-i birləşdirmək üçün istifadə olunur. Birlesdirme emeliyyat eyni sutundaki eyni deyerlere esaslanir. 

import pandas as pd

data1 = {
    "Emp Id" : [ "E01", "E02", "E03", "E04", "E05", "E06"],
    "Names"  : [ "Jorc", "Bob", "Marry", "John", "David", "Mark"],
    "Age"    : [ 34, 56, 23, 44, 32 ,36]
}

# Eger E07 olsaydi onda oxsar deyerler birlescekdi oxsar olmuyanlar nezere alinmayacaqdi. Yeni E06 ve E07 xaric diger oxsar deyerler birlesecekdi.
data2 = {
    "Emp Id" : [ "E01", "E02", "E03", "E04", "E05", "E06"],
    "Salary"  : [ 45000, 56000, 34000, 30000, 50000, 62000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(pd.merge(df1, df2))