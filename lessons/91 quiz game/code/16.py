def yeni_oyun():
    texminler = []
    dogru_texminler = 0
    sualin_nomresi = 1

    for acarlar in sual:
        print("----------------------")
        print(acarlar)
        for i in cavablar[sualin_nomresi-1]: 
            print(i)
        texmin = input("Daxil edin (A, B, C veya D): ")
        texmin = texmin.upper()
        texminler.append(texmin)
        dogru_texminler += suali_yoxla(sual.get(acarlar), texmin)
        sualin_nomresi += 1 
    xal_goster(dogru_texminler, texminler)

def suali_yoxla(dogruCavab, bizimTexminimiz):
    if dogruCavab == bizimTexminimiz:
        print("Dogru")
        return 1
    else:
        print("Yanlis")
        return 0
def xal_goster(dogru_cavablar, texminlerimiz):
    print("-------------------------")
    print("Netice: ")
    print("-------------------------")

    print("Cavablar: ", end=" ")
    for i in sual:  
        print(sual.get(i), end=" ")
    print()

    print("Texminlerimiz: ", end=" ")
    for i in texminlerimiz: 
        print(i, end=" ")
    print()

    derece = int((dogru_cavablar/len(sual)) * 100) 
    print("Dogru texmin derecemiz: " + str(derece) + "%")

#//! 1 - while konstruksiyasi default olaraq True oldugu ucun yeniden_oyna() funksiyasi çagrilir ve input() sahesine deyer girmeyimiz
# istenilir. Eger if sorgusunda muqayise etdiyimiz deyer dogru olarsa, onda True qayidir ve while konstruksiyasi yeni_oyun() funksiyasini
# yeniden cagirir. Eger False olarsa onda while konstruksiyasi işini dayandirir ve ekrana print() metodu sagol yazdirir. 
def yeniden_oyna():
    sorgu = input("Yeniden oynamaq isteyirsen mi? (Beli / Xeyr) : ").upper()
    if sorgu == "BELI":
        return True
    else:
        return False

sual = {
    "Python dilini kim yaradib? " : "A",
    "Python necenci ile yaranib? " : "B",
    "Python adi, hansi komedi klubun adindan ilhamlanmisdir? " : "C",
    "Dunya yuvarlaqdir mi? " : "A",
}
cavablar = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]
]
yeni_oyun()

while yeniden_oyna():
    yeni_oyun()

print("Sagol!!!!!!!")