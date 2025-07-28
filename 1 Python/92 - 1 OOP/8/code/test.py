# klass-lar onun ucun yaxwidir ki, eyni bir klasin birden cox obyektini yaratmaq ve
# her defe ferqli deyerler vermek mumkundur.


from masin import Masin

masin1 = Masin("Renault", "Renault Arkana", 2024, "qara")
masin2 = Masin("BMW", "M5", 2024, "ag")

print(masin2.hazirlamaq)
print(masin2.model)
print(masin2.ili)
print(masin2.rengi)

masin2.surmek()
masin2.dayanmaq()


