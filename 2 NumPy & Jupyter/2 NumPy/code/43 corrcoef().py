
#! corrcoef() metodu, iki və ya daha çox array yaxud deyisken arasında korrelyasiya matrisini hesablamaq üçün istifadə olunur.

# Korrelyasiya matrisi nədir ? Bunu izah etemeden once bezi diger terminlere baxaq. Mesel ucun:

# 1) Korrelyasiya əmsalı nədir ? -  iki və ya daha çox array yaxud deyisken arasında mütənasiblik varmi yoxmu, eger varsa bu munasibaet ne qeder 
# gucludur yaxud zeifdir deye teyin etmekde istifade edilen qaydaya korrelyasiya əmsalı deyilir.

# 2) Mütənasiblik nədir ? - iki kəmiyyətdən birinin artması yaxud azalması ilə o biri kəmiyyətində eyni dərəcədə artması yaxud azalmasıdır.
# Mesel ucnu: qazi artirdiqca qaza verilecek pulda artir.    Bu düz mütənasiblikdir.
# Mesel ucnu: masinin sureti artirdiqca gedeceyi yol azalir. Bu ters mütənasiblikdir.

# Basqa cumle ile birdaha izah edek: 2 ferqli array yaxud deyisken deyerleri arasinda olan benzerliyin cox yaxud az oldugunu ehtimal eden
# qaydaya korrelyasiya əmsalı deyilir. Bunun ucun -1, 1 ve 0 əmsallarindan (ededlerinden) istifade edilir.

# -1   - tərs mütənasib əlaqəni təmsil edir. Yeni, korrelyasiya -1 olarsa bu elaqenin oldugu yalniz ters mutenasib elaqenin oldugu menasina gelir.
#  1   - mütənasib əlaqəni təmsil edir. Yeni, korrelyasiya 1 olarsa bu elaqenin oldugu yalniz mutenasib elaqenin oldugu menasina gelir.
#  0   - əlaqənin olmaması deməkdir.

# 1 pozitiv elaqe vardir demekdir. 0-dan yuxari 1-e yaxinlasdiqca, bu deyerler arasinda munasibetin ne qeder pozitiv guclu artidigini bildirir.
# -1 neqativ elaqe vardir demekdir. 0-dan asagi -1-e yaxinlasdiqca, bu deyerler arasinda munasibetin ne qeder neqativ guclu artidigini bildirir.
# 0 hec elaqe yoxdur demekdir.


# Korrelyasiya matrisi array-lar yaxud variable-lar arasında olan fərqi eks etdiren cedveldir. corrcoef() metodu bu deyerleri muqayise edir ve
# korrelyasiya emsali qaytarir. 


import numpy as np

tutun_istifadesi = [  30, 50, 10, 30, 50, 40  ]
olum_hallari     = [  100, 120, 70, 100, 120, 112  ]


print(  np.corrcoef( [tutun_istifadesi,   olum_hallari] )  )                # [   [1.     0.99015454]          [0.99015454     1.]   ]        

# 1ci setrdeki 1ci sutun 'tutun_istifadesi'-nin 'tutun_istifadesi' ile olan muqayisesidir. Bu hemise 1 qaytarir.
# 2ci setrdeki 2ci sutun 'olum_hallari'-nin     'olum_hallari'     ile olan muqayisesidir. Bu hemise 1 qaytarir.
# Setrlerdeki diger sutunlar ise 'tutun_istifadesi' ve 'olum_hallari' arasindaki muqayisedir.

# 1ci deyer 1ci deyernen, 2ci deyer 2ci deyernen ve.s muqayise edilir.