def yeni_oyun():
    #//! 3 variable yaratdiq. 
    texminler = []
    dogru_texminler = 0
    sualin_nomresi = 1

    for acarlar in sual:
        print("----------------------")
        print(acarlar)
        #//! Bu 0,1,2 ve 3-un manual yox avtomatik cavablar list-ine yazilmasi ucun,  avtomatik 'sualin_nomresi' adli
        # variable-i her dongude bir-bir artirmaliyiq. Buna increment deyirler. 
        for i in cavablar[sualin_nomresi-1]: 
            print(i)
        sualin_nomresi += 1 # sualin_nomresi = sualin_nomresi + 1
        # 1 = 1 + 1 = 2
        # 2 = 2 + 1 = 3
        # 3 = 3 + 1 = 4
        # Bize lazim olan indeksler ise 0,1,2 ve 3 oldugu ucun, sualin_nomresi-1 deyerek her artan deyerden 1 cixiriq 
        # ve bize lazim olan indeksleri aliriq.
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
