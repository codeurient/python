# pass - oturmek, kecirmek kimi qebul edile biler

# qutu in telefon_nomre ne demekdir ? 

# Yeni "telefon_nomre" variable-inda olan deyerlerin hamisi tek-tek
# "qutu" variable-ina verilsin

# if yeni eger bu "qutu" variable-inin icinde olan her hansisa bir deyer
# == (beraber) olarsa "-" defis isaresine onda pass yeni nezere alma
# ve devam et. 

# else yeni eks teqdirde "qutu" variable-inda qalan diger deyerleri prtin() metodu ile 
# ekrana yazdir.

telefon_nomre = "123-456-7890"

for qutu in telefon_nomre:
    if qutu == "-":
        pass
    else:
        print(qutu, end="")


