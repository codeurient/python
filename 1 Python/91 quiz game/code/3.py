 #//! 1. Ilk once ferqli funksiyalar yaradiriq ki, 
def yeni_oyun():
    for acarlar in sual:
        print("----------------------")
        print(acarlar)
# 
def suali_yoxla():
    pass
# 
def xal_goster():
    pass
# 
def yeniden_oyna():
    pass

#//! 2
sual = {
    "Python dilini kim yaradib? " : "A",
    "Python necenci ile yaranib? " : "B",
    "Python adi, hansi komedi klubun adindan ilhamlanmisdir? " : "C",
    "Dunya yuvarlaqdir mi? " : "A",
}


#//! 3
cavablar = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],

    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],

    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],

    ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]
]

#//! 4
# yeni_oyun() funksiyasini 'sual' dict-inin ustunden goturub altina yerlesdiririk ve kodumuz isleyir.


yeni_oyun()