# Indi ise bayaq yazdigimizin eynisini yaziriq. Ancaq daha qisa yol ile.

yemekler = list()

# while konstruktorunun yaninda True yazmasaq bele O, hemise varsayilan deyer
# True qaytardigi ucun hemin True sozunu sile bilerik.
while yemek := input("Hansi yemeyi sevirsiz?: ") != "cix":
    # 1. Burda eyni vaxtda hem sonsuz dongu yaradiriq.
    # 2. "yemek" variable-ina input() sahesine girilen deyeri veririk.
    # 3. != "cix" Eger beraber deyilse girilen deyer "cix" sozune yazaraq muqayise apaririq.
    yemekler.append(yemek)

print(yemekler)