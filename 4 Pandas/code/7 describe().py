# describe() - DataFrame-də rəqəmli sütunların əsas statistikasının qısa məzmununu qaytarır. 
# (Umumu cedvelde 14 sutun vardir ancaq sadece reqem olan 4 sutun movcuddur.)
# Bu statistikaya kardinallıq, orta, standart kənarlaşma, minimum, maksimum və kvartil dəyərlər daxildir.


# 1) standart kənarlaşma - 
# 2) kvartil - dordde bir demekdir.
# 3) sütunların  sayı
# 4) hər sütundakı data-larin tipleri (Dtype)
# 5) sıfırdan fərqli dəyərlərin sayı
# 6) verilənlərin tutduğu yaddaşın miqdarı (memory usage 109.5+ KB)

# count - data-larin sayini verir
# mean  - Hər sütundakı orta dəyər hansıdırsa onu qaytarır
# min   - Hər sütundakı minimum dəyər hansıdırsa onu qaytarır
# 25%   - Hər sütundakı dəyərlərin 25%-ni ehtiva edən aşağı kvartil (Q1).
# 50%:  - Hər sütundakı dəyərlərin 50%-ni ehtiva edən aşağı kvartil (Q2).
# 75%:  - Hər sütundakı dəyərlərin 75%-ni ehtiva edən aşağı kvartil (Q3).
# max:  - Hər sütundakı maksimum dəyər hansıdırsa onu qaytarır
# std:  - standart kənarlaşma


import pandas as pd


melumatlar = pd.read_excel('Datasets-main/ESD.xlsx')

print(melumatlar)
print(melumatlar.describe())