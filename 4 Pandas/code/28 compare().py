# comparea() - iki DataFrame-i müqayisə etmək və aralarındakı fərqləri gostermek üçün istifadə olunur.

import pandas as pd

data = {
    "Fruits"    : [ "mango", "apples", "banana", "papaya" ],
    "Price"     : [ 100, 150, 50, 35 ],
    "Quantity"  : [ 15, 10, 10, 3 ]
}

df1 = pd.DataFrame(data)
print(   df1   )

print('*****************************************************')

df2 = df1.copy()

df2.loc[0, "Price"] = 120
df2.loc[1, "Price"] = 175
df2.loc[2, "Price"] = 30
df2.loc[0, "Quantity"] = 7
df2.loc[1, "Quantity"] = 1
df2.loc[2, "Quantity"] = 4
print(df2)

print('*****************************************************')

print(  df1.compare(df2)  )