# join() funksiyası standart olaraq iki fərqli DataFrames birləşdirir. Yəni iki eyni DataFrame-i birləşdirmir.

import pandas as pd

# Eger her iki DataFrame-de sutun adlari eyni olsa xeta alardiq. Tebii ki, eyni adlar olduqda ne etmek lazimdir 
# bunu parametrler ile teyin etmek olar. Yəni, hansi formada birlesdirsin, hansini hansina birlesdirsin ve.s.
data1 = {
    "Emp Id1" : [ "E01", "E02", "E03", "E04", "E05", "E06"],
    "Names1"  : [ "Jorc", "Bob", "Marry", "John", "David", "Mark"],
    "Age1"    : [ 34, 56, 23, 44, 32 ,36]
}

data2 = {
    "Emp Id2" : [ "E07", "E08", "E09", "E10", "E11", "E12"],
    "Names2"  : [ "Baris", "Artur", "Jery", "Tom", "Lukas", "Beny"],
     "Age2"   : [ 34, 56, 23, 44, 32 ,36]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

yeni_cedvel = df1.join(df2)


print(   yeni_cedvel   )