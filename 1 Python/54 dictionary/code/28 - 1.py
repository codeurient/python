# dumps() - bu metod dict tipinde olan elementleri JSON formatina cevirir. (JavaScript Object Notation)     #! serialization
# JSON formatina cevrilen elementler artiq tip olaraq string olur.

# Beləliklə, JSON formatina çevrilen məlumatları, proqramlar arasında ötürmək və ya her hansisa faylin yaddasina yazmaq olar. 

# Proqramlar arasında ötürmək dedikde, yeni, PYTHON proqramlasdirma dilinde, JSON formatina cevrilen melumati 
# JavaScript ve yaxud basqa proqramlasdirma diline oturmek olar. JSON onsuzda bunun ucun istifade edilen bir
# qaydadir. Hemin melumatlar JavaScript proqramasdirma diline gelir ve biz yeniden hemin melumatlari o proqramlasdirma
# dilinde olan JSON metodu ile bize lazim olan formata geri cevirerek istifade ede bilerik.

import json

telebe_melumatlari = {"ad": "Kamal", "yash": 16, "bal": 655}
print(type(telebe_melumatlari))

# JSON formatina cevrilen melumatlarin tipi STRING olur. 
melumat = json.dumps(telebe_melumatlari)
print(melumat)












