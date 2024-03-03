# popitem() - bu metod lugetin icindeki en sonuncu acar ve deyeri silmek ve hemin silinen acar ve deyeri
# elde etmek ucun istifade edilir.

# 1. luget yaradiriq
luget = {'a': 1, 'b': 2, 'c': 3}

# popitem() metodu ile hemin lugetin icinden en sonuncu acar soz ve deyeri silirik.
# Silinen acar soz ve deyer hansidirsa, hemin acar soz ve deyer 'yeni_luget' adli variable icine yazilir.
yeni_luget = luget.popitem()

# silinen acar soz ve deyeri elde edirik
print(yeni_luget)


# Birinci lugetin icine baxiriq ki, silindimi yoxsa yox.
print(luget)
