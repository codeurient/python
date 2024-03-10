# Vaxt ile islemek ucun time modulunu import etmeliyik.
import time

# ctime() - current time - hal hazirki vaxti elde etmek ucun istifade edilir.

# parametr olaraq 1 000 000 000 (1 milyard) yazdiqda ise, Epoxadan 1 milyard saniye kecmisdir demekdir.
# Epoxadan 1 milyard saniye sonra gelen tarix hansidirsa hemin tarixi elde edirik: #! Sun Sep  9 06:46:40 2001

# Yeni, parametr olaraq number veririk ve bu number saniyeleri bildirir.
print(   time.ctime(1000000000)   )