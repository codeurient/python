import random
# Eger her defe play duymesine basaraq kodu işə salmaq istemirikse onda burda olan butun kodlari sonsuz donguse saliriq. Bes sonsuz donguden ne vaxt cixir?
while True:
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
    # Bu asagida yazdigimiz input saheside sonsuz dongunun icindedi ve if sorgusu ile deyirik ki, eger hemin saheye yazilan deyer Beli sozune beraber deyilse
    # onda break ol yeni sonlan. Meselen, Beli != Beli bu FALSE verir ve while dongusu yeniden isleyir. Cunki true verse idi break dongunu sonlandiracaqdi.
    # if sorgusunun TRUE vermesi ucun Beli stringinden ferqli deyer yazmagimiz kifayetdir.  
    yeniden_oynayaqmi = input("Yeniden oynamaq isteyirsenmi? (Beli/Xeyr): ").lower()
    if yeniden_oynayaqmi != "beli":
        break
