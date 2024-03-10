# info() - verilənlər cedveli haqqinda qısa məlumat əldə etmək üçün istifadə olunur.

# 1) sətirlerin sayı
# 2) sütunların  sayı
# 3) hər sütundakı data-larin tipleri (Dtype)
# 4) sıfırdan fərqli dəyərlərin sayı
# 5) verilənlərin tutduğu yaddaşın miqdarı (memory usage 109.5+ KB)




import pandas as pd


melumatlar = pd.read_excel('Datasets-main/ESD.xlsx')

print(melumatlar)
print(melumatlar.info())