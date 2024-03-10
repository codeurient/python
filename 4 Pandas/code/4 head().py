# head() - verilənlərin ilk bir neçə sətirini göstərmək üçün istifadə olunur. 
# Varsayılan olaraq, head() verilənlərin ilk 5 sırasını göstərir. Bu, bütün verilənləri
# göstərmədən verilənlər və onun strukturu ilə tez tanış olmaq üçün faydalıdır.

# head(10) - 5 den cox melumat gostermek istedikde bunu parametrde qeyd etmek mumkundur.



import pandas as pd


melumatlar = pd.read_excel('Datasets-main/ESD.xlsx')

print(melumatlar.head())