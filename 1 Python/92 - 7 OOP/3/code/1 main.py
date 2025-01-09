class Duzbucaqli:
    def __init__(self, uzunluq, en):
        self.uzunluq = uzunluq
        self.en = en

class Kvadrat(Duzbucaqli):
    def __init__(self, uzunluq, en):
        super().__init__(uzunluq, en)

    #! sahe() adinda elave bir metod yaradiriq ki, elde etdiyimiz deyerleri bir-birine vuraq.
    # kvadratin sahesini hesabladiqda onun "uzunlugu * enine "
    def sahe(self):
        return self.uzunluq*self.en

class Kub(Duzbucaqli):
    def __init__(self, uzunluq, en, hundurluk):
        super().__init__(uzunluq, en)
        self.hundurluk = hundurluk

    #! hecm() adinda elave bir metod yaradiriq ki, elde etdiyimiz deyerleri bir-birine vuraq.
    # kubun hecmini hesabladiqda onun "uzunlugu * enine * hundurluyune"
    def hecm(self):
        return self.uzunluq*self.en*self.hundurluk
    
kvadrat = Kvadrat(3, 3)
kub = Kub(3, 3, 3)

print(kvadrat.sahe())
print(kub.hecm())