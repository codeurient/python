# Eyni tapsirigin ferqli yollar ile uzun ve daha qisa sekilde hell edilmesi.

telebeler = [100, 90, 80, 70, 60, 50, 40, 30, 0]

# for dongusu "telebeler" list-inden deyerleri "i" variable-ina verir ki, muqayise edek.
# 60-dan boyuk olan deyerler "i" variable-inda yaddawa yazilaraq "kecen_telebeler" adli 
# list icine elave edilir.
kecen_telebeler = [ i for i in telebeler if i >= 60 ]

print( kecen_telebeler )



#? Buda dusturumuzdur.
#! list = [ expression for item in iterable if conditional ]