# melt() funksiyasi DataFrame-i "geniş" formatdan "uzun" formata çevirmək üçün istifadə olunur

import pandas as pd

data = {
    "Names"   : [ "John", "Ben", "David", "Peter" ],
    "Houses"  : [ "red", "blue", "green", "red" ],
    "Grades"  : [ "3rd", "8th", "9th", "3rd" ]
}

df = pd.DataFrame(data)

print(  df  )
print("*******************************************************")

print(df.pivot(columns="Names", values="Houses"))
print("*******************************************************")

print(pd.melt(df, id_vars=["Names"], value_vars=["Houses"]))
print("*******************************************************")

print(pd.melt(df, id_vars=["Names"], value_vars=["Houses", "Grades"], var_name="Houses&Grades", value_name="values"))