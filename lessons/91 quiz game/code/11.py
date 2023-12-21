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
        # //! 1
        # get() metodu dict-in icinden deyerleri elde etmek ucun istifade edilir. Bu metoda biz
        # acar sozu yaziriq ve hemin acar soze mexsus deyeri elde edirik. Elde etdiyimiz deyeri 
        # parametr olaraq suali_yoxla() funksiyasina otururuk ve asagida print() metodu ile 
        # ekrana yazdiririq ki, gorek hemin deyeri elde ede bildik mi bilmedik mi.
        suali_yoxla(sual.get(acarlar))
        
        sualin_nomresi += 1 
#//! 2
def suali_yoxla(a):
    print(a)
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