from masin import Masin

masin1 = Masin("Renault", "Renault Arkana", 2024, "qara")
masin2 = Masin("BMW", "M5", 2024, "ag")

# Bele dedikde sadece masin1 obyektine mexsus xassenin deyerini deyismis oluruq
# masin2 obyekti ucun ise hemin xassenin deyeri 4 olaraq qalir
#//! masin1.teker = 2

# Eger Klas adi ile hemin xasseye muraciet ederek deyeri deyisersek onda hemin 
# klasin butun  obyektleri ucun teker xassesinin deyeri deyisilmis hesab edilecek.
Masin.teker = 3

print(  masin1.teker  )
print(  masin2.teker  )