import pandas as pd

qutu = { 'Month' : [ 'January', 'Feburary', 'March', 'April' ]}


# List yaradiriq. Icinde 4 deyer var. Deyerlerin indeksi beledir:
# 0 - 'January'
# 1 - 'Feburary'
# 2 - 'March'
# 3 - 'April'

# Kvadrat moterize ile [] 'qutu' adli list-e muraciet edirik. Indekslerin vasitesi ile ise lazimli
# deyeri cagirirq. Araliqda olan deyerleri elde etmek ucun Indexing[] qaydasindan istifade edirik.
print(   qutu[0]   )

# 0-dan 3-e qeder olan deyerleri elde edirik. 3 daxil deyil.
print(   qutu[0:3]   )