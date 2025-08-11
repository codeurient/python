import random

secmek = ["qayci", "kagiz", "qaya"]
komputer = random.choice(secmek)

oyuncu = None
while oyuncu not in secmek:
    oyuncu = input("qayci, kagiz yoxsa qaya ?: ").lower()

if oyuncu == komputer:
    print("Komputer: ", komputer)
    print("Oyuncu: ", oyuncu)
    print("Beraber!")

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