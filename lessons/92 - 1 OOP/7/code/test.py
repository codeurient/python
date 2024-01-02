from masin import Masin

masin1 = Masin("Renault", "Renault Arkana", 2024, "qara")

print(masin1.hazirlamaq)
print(masin1.model)
print(masin1.ili)
print(masin1.rengi)

# Yaxud metodlara da muraciet ederek print() metodunun sahib 
# oldugu metni ekrana yazdira bilerik. Burda print() yazmaga ehtiyac yoxdur
# ceunki print() metodu klas-da olan metodun icinde istifade edilib.
masin1.surmek()
masin1.dayanmaq()