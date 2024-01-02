class Heyvan:
    canli = True

    def yemek(self):
        print("Bu heyvan yemek yeyir")

    def yatmaq(self):
        print("Bu heyvan yatir")

class Dovsan(Heyvan):
    pass
class Baliq(Heyvan):
    pass
class Sahin(Heyvan):
    pass

dovsan = Dovsan()
baliq  = Baliq()
sahin  = Sahin()

# Indi hansi klasin obyektine muraciet etsekde Ana klas olan Heyvan klasindan 
# istenilen xasseni ve metodu hemin subclass ucun istifade ede bilerik.

print(dovsan.canli)
baliq.yemek()
sahin.yatmaq()