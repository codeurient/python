from masin import Masin

# arqumentleri teyin etdikden sonra obyektin adini yazaraq xasseleri cagira
# ve hemin xassenin sahib oldugu deyeri ekrana yazdira bilerik.
masin1 = Masin("Renault", "Renault Arkana", 2024, "qara")

print(masin1.hazirlamaq)
print(masin1.model)
print(masin1.ili)
print(masin1.rengi)

masin1.surmek()
masin1.dayanmaq()