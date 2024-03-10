import random

secmek = ["qayci", "kagiz", "qaya"]
komputer = random.choice(secmek)

oyuncu = None
while oyuncu not in secmek:
    oyuncu = input("qayci, kagiz yoxsa qaya ?: ").lower()

# Eger eyni deyerleri girmisikse onda ekrana hem komputerin hem bizim girdiyimiz deyerleri 
# hemde eyni deyerleri girdiyimiz ucun berabere qaldiq deye mesaj yazdiririq.
if oyuncu == komputer:
    print("Komputer: ", komputer)
    print("Oyuncu: ", oyuncu)
    print("Beraber!")

# Eger biz deyer olaraq "qaya" yazsaq sorgu icinde sorgu ile komputerin girdiyi deyerle muqayise edirik.
# komputer eger kagiz tutubdusa biz uduzuruq eger qayci tutubdusa biz uduruq. Eyni deyer olsa ise yuxarda olan kod isleyir.
elif oyuncu == "qaya":
    if komputer == "kagiz":
        print("Komputer: ", komputer)
        print("Oyuncu: ", oyuncu)
        print("Sen uduzdun!")
    if komputer == "qayci":
        print("Komputer: ", komputer)
        print("Oyuncu: ", oyuncu)
        print("Sen uddun!")

elif oyuncu == "qayci":
    if komputer == "qaya":
        print("Komputer: ", komputer)
        print("Oyuncu: ", oyuncu)
        print("Sen uduzdun!")
    if komputer == "kagiz":
        print("Komputer: ", komputer)
        print("Oyuncu: ", oyuncu)
        print("Sen uddun!")

elif oyuncu == "kagiz":
    if komputer == "qayci":
        print("Komputer: ", komputer)
        print("Oyuncu: ", oyuncu)
        print("Sen uduzdun!")
    if komputer == "qaya":
        print("Komputer: ", komputer)
        print("Oyuncu: ", oyuncu)
        print("Sen uddun!")