# funksiyalarin deyer qaytarmasi. return.

# return ingilis dilinde qaytarmaq demekdir. Funksiyalarda ne ise yariyir bu return ?

# bura qeder yazdigimiz diger numunelerde sadece 1 funksiya var idi ve hemin funksiyanin
# neticesi ekrana yazdirilirdi. Ancaq ele ola bilerki bizim 1 den cox funksiyamiz olsun ve
# 1ci funksiya toplama emeliyyati icra etsin, 2ci funksiya ise toplamadan qayidan neticeni 
# vurma emeliyyati ucun istifade etsin. Meselen:


def toplama(eded1, eded2):
  return eded1 + eded2


# Yuxarida olan funksiya toplama emeliyyati gorur. Indi ise asagida vurma emeliyyati edecek
# funksiyani yaradiriq. Bu 2ci funksiyanin icinde 1ci funksiyani cagiririq.


def vurma(birinciEded, ikinciEded):
  return toplama(birinciEded, ikinciEded) * toplama(birinciEded, ikinciEded)

# Burda 2ci funksiyanin parametrlerine 3 ve 5 veririk. Hemin parametrler deyere olaraq 1ci funksiyaya 
# gonderilir ve orda toplandiqdan sonra 1ci funksiya neticeni return edir yeni qaytarir. Netice 3+5=8 dir.
# Eyni funksiyani iki defe cagirmisiq deye 2 defe 8 return olacaq. Ikinci funksiya ise return olan neticeni 
# vuracaq. Yeni, 8*8=64 return edecek. Return olan neticeni ise asagida print() metodu ile ekrana yazdiririq.
print(   vurma(3, 5)   )