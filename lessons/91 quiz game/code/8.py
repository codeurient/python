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
        #//! input sahesine daxil etdiyimiz deyerlerin her zaman texmin variable-ina boyuk olaraq
        # gonderilmesi ucun upper() metodundan istifade edirik.
        texmin = texmin.upper()
        sualin_nomresi += 1 
# 
def suali_yoxla():
    pass
# 
def xal_goster():
    pass
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
