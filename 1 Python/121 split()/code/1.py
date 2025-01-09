# split() - string-i müəyyən simvol əsasında alt sətirlərə bölmək üçün istifadə olunur.

# Yeni string icinde herfler yaxud sozler her hansisa bir simvol vasitesi bolgulere ayrilarsa,
# bu simvollar arasinda yerlesen herf ve sozleri split() metodu ile ayirmaq olar.  

# Bu metod netice olaraq list() qaytarir.


metn1 = '#Alma##Armud#Heyva###Nar####'
print(   metn1.split('#')   )




metn2 = '#Alma#Armud#Heyva#Nar#'
print(   metn2.split('#')   )
