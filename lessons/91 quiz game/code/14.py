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
        # //! 3 - Her dogru cavab verdikde 1 qayidanda (0 = 0 + 1, 1 = 1 + 1, 2 = 1 + 2, 3 = 1 + 3 ) olacaq
        dogru_texminler += suali_yoxla(sual.get(acarlar), texmin)
        sualin_nomresi += 1 
    #//! 4 - Butun suallara cavab verdikden sonra xal_goster() funksiyasi cagrilacaq 
    xal_goster(dogru_texminler)

def suali_yoxla(dogruCavab, bizimTexminimiz):
    if dogruCavab == bizimTexminimiz:
    #//! 1 - Funksiya eger deyerler beraber olarsa hem ekrana 'Dogru' stringini yazdirir
    # Hemde hemin bu suali_yoxla() funksiyasi her defe 1 deyerini qaytarir.
    # Her defe 1 qayidanda ve eger 4 sual versa bu 4 defe 1 qayidacaq demekdir. 
        print("Dogru")
        return 1
    else:
    #//! 2 - Eks halda 'Yanlis' stringi ekrana yazdirilacaq ve suali_yoxla() funksiyasi her  defe 0 deyerini qaytaracaq.
        print("Yanlis")
        return 0
#//! 5 - Ve burda nece suala dogru cavab vermisik deye gormek ucun print() metodu ile neticeni ekrana yazdiririq. 
def xal_goster(a):
    print(a)
# 
def yeniden_oyna():
    pass

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