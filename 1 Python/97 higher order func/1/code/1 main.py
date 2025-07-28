# Funksiyalarin arqument kimi diger funksiya-ya gonderilerek istifade edilmesi.

def boyuk(metn):
    return metn.upper()


def kicik(metn):
    return metn.lower()







# 3cu funksiyamizin parametri diger funksiyalari qebul etmek ucundur.
# Bu gonderilen funksiyalarin heresi bir is gorur ancaq onlarin gorduyu ferqli islerin
# neticesi burda gorduyumuz 3cu funksiya ile ekrana yazdirilir.
def ekranaYazdir(funksiya):
    # Elde etdiyimiz funksiyani deyiskene oturerek print() ile ekrana yazdiririq.
    metn = funksiya("SalaM")
    print(metn)

ekranaYazdir(boyuk)
ekranaYazdir(kicik)