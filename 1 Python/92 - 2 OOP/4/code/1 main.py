class Heyvan:
    canli = True

    def yemek(self):
        print("Bu heyvan yemek yeyir")

    def yatmaq(self):
        print("Bu heyvan yatir")


# Subclass-lar ucun unikal metodlar yarada ve onlari cagiraraq istifade ede bilerik
class Dovsan(Heyvan):
    def qacmaq(self):
        print("Bu dovsan qacir")

class Baliq(Heyvan):
    def uzmek(self):
        print("Bu baliq uzur")

class Sahin(Heyvan):
    def ucmaq(self):
        print("Bu sahin ucur")

dovsan = Dovsan()
baliq  = Baliq()
sahin  = Sahin()

dovsan.qacmaq()
baliq.uzmek()
sahin.ucmaq()