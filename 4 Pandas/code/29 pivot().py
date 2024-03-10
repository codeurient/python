# pivot() - funksiyasi DataFrame-də verilənlərin formasını dəyişdirmək üçün istifadə olunur. 
# pivot() funksiyasi, məlumatları "uzun" formatdan "geniş" formata çevirməyə imkan verir.

import pandas as pd

data = {
    "keys"    : [ "k1", "k2", "k1", "k2" ],
    "Names"   : [ "John", "Ben", "David", "Peter" ],
    "Houses"  : [ "red", "blue", "green", "red" ]
}

df = pd.DataFrame(data)

print(  df  )

print("*******************************************************")

# Burda pivot() metodu, "keys", "Names" ve "Houses" deyerlerini daha rahat bir vizual yaradaraq yeni DataFrame 
# cedveline cevirmek ucun istifade edilir.
print(df.pivot(index="keys", columns="Names", values="Houses"))