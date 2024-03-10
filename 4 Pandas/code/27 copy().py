# copy() - funksiyası orijinal obyektin surəti olan yeni DataFrame obyekti yaradır.

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
print(df2)