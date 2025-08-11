def yeni_oyun():

    for acarlar in sual:
        print("----------------------")
        print(acarlar)
        #//! Burda 2ci for dongusu 1ci for dongusunun icinde oldugu ucun, 1 defe yuxarda olan for dongusu isleyende
        # onun icinde olan 2ci for dongusu "cavablar" list-inin icindeki deyer qeder tekrarlanacaq. Yeni, 4 defe.
        for i in cavablar[0]: 
            print(i)
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
# //! 
# yeni_oyun() adinda olan funksiyamizi cavablar list-imizin altina keciririk ki, yene xeta almayaq. 
# Cunki, hemin funksiyanin icinde for dongusu ile butun cavablari ekrana yazdirmaq isteyirik ki, 
# kodumuzun isleyib islemediyini gorek.
yeni_oyun()