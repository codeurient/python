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
    #//! 1 - Birinci parametr kimi necedene dogru texin etdik onu, ikinci parametr kimi oz texminlerimizi list kimi gonderirik. 
    xal_goster(dogru_texminler, texminler)

def suali_yoxla(dogruCavab, bizimTexminimiz):
    if dogruCavab == bizimTexminimiz:
        print("Dogru")
        return 1
    else:
        print("Yanlis")
        return 0
#//! 2 - Bu funksiyanin icinde hem dogru cavablari hem bizim texminlerimizi hemde neçe dogru texmin etmisik onu faiz ile ekrana yazdiririq.
def xal_goster(dogru_cavablar, texminlerimiz):
    print("-------------------------")
    print("Netice: ")
    print("-------------------------")

    print("Cavablar: ", end=" ")
    for i in sual:  #//! 3 - sual dict-dir ve get() metodu dict-in deyerlerini elde etmek ucundur. get() icinde acar sozler yazilanda deyerleri elde edirik.
        print(sual.get(i), end=" ")
    print()

    print("Texminlerimiz: ", end=" ")
    for i in texminlerimiz: #//! 4 - texminlerimiz list-dir ve deyerleri i variable-ina gondererek ekrana yazdiririq.
        print(i, end=" ")
    print()

    derece = int((dogru_cavablar/len(sual)) * 100) #//! 5 - Dogru cavablarin sayini faize cevirerek ekrana yazdiririq.
    print("Dogru texmin derecemiz: " + str(derece) + "%")

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