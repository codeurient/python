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
# {} - dict yaradiriq ve icinde "acar" : "deyer" qeyd edirik. Bu dict sullari saxlamaq ucundur
# dict icindeki deyerleri ekrana yazdirmaq ucun acar sozu kvadrat moterize icinde qeyd edirik.
# print( sual["Dunya yuvarlaqdir mi? "] )
sual = {
    "Python dilini kim yaradib? " : "A",
    "Python necenci ile yaranib? " : "B",
    "Python adi, hansi komedi klubun adindan ilhamlanmisdir? " : "C",
    "Dunya yuvarlaqdir mi? " : "A",
}

#//! 3
# Burda ise cavablari saxlamaq ucun list yaradiriq - []
# list icindeki deyerleri ekrana yazdirmaq ucun kvadrat moterize icinde hemin deyerin indeksini qeyd edirik.
# print(cavablar[0][2])
cavablar = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],

    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],

    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],

    ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]
]

#//! 4
# yeni_oyun() funksiyasinin icinde 'for' dongusu ile 'sual' dict-inin acar sozlerini ekrana yazdiririq.
# Funksiyanin islemesi ucun onu cagirmaq lazimdir. Lakin funksiyani yanliw yerde cagirsaq xeta verecekdir.
# Meselen, 'sual' dict-inin ustunde cagirsaq funksiya hemin 'sual' dict-ini gormuyeceyi ucun xeta alariq.
# Xeta almamaq ucun ise funksiyani 'sual' dict-inin altinda cagirmaq lazimdir.




yeni_oyun() 
