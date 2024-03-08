# concat() funksiyasi iki və ya daha çox DataFrames-i birləşdirmək üçün istifadə olunur.

import pandas as pd

data1 = {
    "Emp Id" : [ "E01", "E02", "E03", "E04", "E05", "E06"],
    "Names"  : [ "Jorc", "Bob", "Marry", "John", "David", "Mark"],
    "Age"    : [ 34, 56, 23, 44, 32 ,36]
}

data2 = {
    "Emp Id" : [ "E07", "E08", "E09", "E10", "E11", "E12"],
    "Names"  : [ "Baris", "Artur", "Jery", "Tom", "Lukas", "Beny"],
     "Age"   : [ 34, 56, 23, 44, 32 ,36]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)


print(   pd.concat([df1, df2])   )