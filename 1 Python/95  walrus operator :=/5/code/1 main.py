# List yaradiriq ki, icine input() sahesine daxil etdiyimiz deyerleri qoyaq.

yemekler = list()

# Sonsuz dongu yaradiriq.
while True:
    yemek = input("Hansi yemeyi sevirsiz?: ")
    # Eger daxil etdiyimiz deyer "cix" olarsa "break" deyerek dongunu dayandiririq.
    if yemek == "cix":
        break
    # Dongu ne qederki dayanmayib, her defe input() metodu bir deyer girmeyimizi
    # isteyecek ve girdiyimiz deyerleri append() metodu ile "list"-e gonderirik.
    yemekler.append(yemek)

# Gonderdiklerimizi dongu dayandiqda gormek ucun "while" konstruksiyasinin colunde
# print() metodu ile ekrana yazdiririq.
print(yemekler)