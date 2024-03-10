# Birden cox klas yarada bilerik
class Masin:
    reng = None

class Motosiklet:
    reng = None

# Bu bir dene funksiya vasitesi ile butun klaslarin obyektlerini qebul ede bilerik.
# Bunun ucun parametrden istifade edirik.
def rengi_deyismek(neqliyyatVasitesi, reng):
    neqliyyatVasitesi.reng = reng

# Klaslarin obyektlerini yaradiriq
masin1 = Masin()
masin2 = Masin()
motor1 = Motosiklet()
motor2 = Motosiklet()

# Funksiyamizi cagiririq ve arqument kimi yuxarda olan klasin obyektini gonderirik.
rengi_deyismek(masin1, "qirmizi")
rengi_deyismek(masin2, "ag")
rengi_deyismek(motor1, "goy")
rengi_deyismek(motor2, "qara")

# Yuxarda yaratdigimiz funksiya ile klasin xassesine 2ci parametrde olan deyeri otururuk ve
# print() metodu icinde klasin obyektini cagiririq, sonra noqte ile hemin klasin xassesini.   
print(masin1.reng)
print(masin2.reng)
print(motor1.reng)
print(motor2.reng)