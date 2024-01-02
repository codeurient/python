# Heyvan adinda klass yaradiriq. Ve butun heyvanlarin ortaq xasselerini ana
# klas icinde qeyd edirik
class Heyvan:

    canli = True

    def yemek(self):
        print("Bu heyvan yemek yeyir")

    def yatmaq(self):
        print("Bu heyvan yatir")

# Burda ise subclass-lari yaradiriq ve her heyvanin ozune aid olan xasselerini 
# qeyd edeceik.
class Dovsan(Heyvan):
    pass
class Baliq(Heyvan):
    pass
class Sahin(Heyvan):
    pass

# Burda ise hemin subclass-larin obyektlerini yaradiriq.
dovsan = Dovsan()
baliq  = Baliq()
sahin  = Sahin()