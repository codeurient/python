dostlar = [("Cavidan", 19),
           ("Seymur" , 18),
           ("Kamal"  , 17),
           ("Nurlan" , 16),
           ("Huseyn" , 21),
           ("Anar"   , 20)]

yash = lambda deyerler : deyerler[1] >= 18

# filter() metodu "dostlar" list-inden bir-bir deyerleri "yash" variable-inin
# icindeki lambda funksiyasina gonderir. Hemin, funksiya indeksi [1] olan 
# deyerleri 18 ededi ile muqayise edir ve True qayidan deyerleri yadda saxlayir.
icki_yoldaslari = list( filter(yash, dostlar) )

for i in icki_yoldaslari:
    print(i)