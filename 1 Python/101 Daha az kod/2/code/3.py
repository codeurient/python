# Eyni tapsirigin ferqli yollar ile uzun ve daha qisa sekilde hell edilmesi.

telebeler = [100, 90, 80, 70, 60, 50, 40, 30, 0]

# Burda if yəni, eger deyerler 60-dan boyuk olarsa deyerek 60-dan boyuk olanlari elde etmisik ve
# else yəni, eks halda yəni, 60-dan kicik olanlari deyerek "FAILED" sozunu elde etmisik ve her iki 
# elde etmis oldugumuz neticeni "kecen_telebeler" adindaki list icinde yazdirmisiq.
kecen_telebeler = [i if i >= 60 else "FAILED" for i in telebeler]

# Imtahandan kecenler ucun Bal kecmeyenler ucun ise FAILED sozu ekrana yazdirilacaqdir.
print( kecen_telebeler )



#? Buda dusturumuzdur.
#! list = [ expression  (if/else) for item in iterable ]