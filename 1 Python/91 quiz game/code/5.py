def yeni_oyun():
    #//! 3 variable yaratdiq. 
    texminler = []
    dogru_texminler = 0
    sualin_nomresi = 1

    for acarlar in sual:
        print("----------------------")
        print(acarlar)
        #//! Bize lazim olan 1ci suala 1ci.... 2ci suala 2ci..... 3cu suala 3cu..... 4cu suala 4cu cavablarin uygun gelmesidir.
        # cavablar list-inin icinde list movcuddur. yeni [ ] var ve onunda icinde [ ] var. 
        # for dongusu avtomatik olaraq list-in icine daxil olur ve 1ci kvadrat moterize itir. 
        # Qalir iceride olan 4 dene listin kvadrat moterizesi. Eger, cavablar[0] yazarsaq onda 1ci list-in icine daxil olariq
        # ve hemin list-in icindeki butun deyerleri 'i' variable-ina  oturmus olariq. Asagida oldugu kimi.
        # Burda 1ci list-in icinde olan deyerler 4 defe tekrarlanir cunki biz sadece 0 yazmisiq. Bu sifir avtomatik olaraq
        # deyismelidir. Her defe el ile 0,1,2,3 yaza bilmerik. Bu reqemleri ele etmeliyik ki, proqram ozu ora qoysun.
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
yeni_oyun()
