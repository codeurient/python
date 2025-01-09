# rindex() - string icinde axtarilan deyerin en sonuncusu hansidirsa hemin deyerin indeksini qaytarir.


deyer = 'salam dunya, salam Python, salam sinif'

print(   deyer.rindex('salam')   )  # 27

# index() - bu metod axtardigimiz deyerin ilk tapilaninin indeksini qaytarirdi. 
# rindex() ise sonuncunu.

# axtarilan deyer tapilmadiqda, xeta mesaji qaytarir: ValueError: substring not found