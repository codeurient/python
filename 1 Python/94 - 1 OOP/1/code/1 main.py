# Bu ders oyreneceyik: Klas obyektlerinin, funksiya vasitesi ile arqument kimi oturulmesi.

# 1) Bir eded Masin adinda klas yaradiriq.
class Masin:
    reng = None

# 2) İki parametr qebul edecek bir funksiya yaradiriq. Bu funksiya Masin klasina aid deyildir,
#    cunki bu funksiya Masin klasinin xaricinde yaradilmisdir. 
def rengi_deyismek(masin, reng):
# 4) Burda masin parametri vasitesi ile Masin obyektinin ozunu cagiraraq noqte ile, onun "reng" adindaki   
#    xassesine muraciet edir ve 2ci parametr vasitesi ile elde etdiyimiz deyeri gonderirik hemin xasseye.
    masin.reng = reng

# 3) Masin klasinin obyektini yaradiriq.
masin1 = Masin()
masin2 = Masin()
masin3 = Masin()

# 4) Funksiyani cagiraraq, obyekti arqument kimi gonderirik 1ci parametre, stringi ise 2ci parametre
rengi_deyismek(masin1, "qirmizi")
rengi_deyismek(masin2, "ag")
rengi_deyismek(masin3, "goy")


print(masin1.reng)
print(masin2.reng)
print(masin3.reng)