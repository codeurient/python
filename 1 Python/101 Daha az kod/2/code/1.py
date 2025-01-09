# Eyni tapsirigin ferqli yollar ile uzun ve daha qisa sekilde hell edilmesi.

telebeler = [100, 90, 80, 70, 60, 50, 40, 30, 0]

# filter() metodu list-in icinden deyerleri lambda funksiyasinin "x" parametrine verir. Sonra hemin "x" parametrinde olan deyerleri 
# muqayise edirik. 60-dan boyuk olanlari yeniden list() metodu ile list-e cevirerek, "kecen_telebeler" adli variable-la gonderirik.
kecen_telebeler = list(   filter(lambda x: x >= 60, telebeler)   )

print( kecen_telebeler )