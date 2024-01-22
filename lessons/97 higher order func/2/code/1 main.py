# Ic-ice funksiya ve 1ci funksiyanin onun icinde olan 2ci funksiyani return etmesi.


# 5. Belelikje hem x-in deyeri 2 olur hemde y-in deyeri 10 olur. 10 / 2 = 5 edir.
def bolen(x):
    def bolunen(y):
        return y / x
    return bolunen

# 1. "bol" variable-ina adı bolen() olan funksiyamizi ve arqument olaraqda 2 veririk.
# 2. Bu sirada adı bolunen() olan funksiyamiz heleki ISLEMIR. Ancaq "x" parametri artiq 2 deyerini alib yadda saxlayib.
# 3. "bol" adindaki variable eslinde bolen() funksiyamizin ozudur.
bol = bolen(2)
# 4. print() metodunda ikinci defe eyni funksiyani cagirdiqda bu artiq bolunen() funksiyasi olur. Cunki bolen() return 
# edir bolunen() adli funksiyamizi. Ve mentiqnen bolunen() funksiyamizi cagirmis hesab edilirik ve hemin bu 10 deyeri de
# aid olur bolunen() funksiyasinin "y" parametrine. 
print(bol(10))