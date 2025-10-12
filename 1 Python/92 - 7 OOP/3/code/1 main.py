class Kalkulyator:
    def __init__(self, uzunluq, en):
        self.uzunluq = uzunluq
        self.en = en

class Kvadrat(Kalkulyator):
    def __init__(self, uzunluq, en):
        super().__init__(uzunluq, en)

    def sahe(self):
        return self.uzunluq*self.en

class Kub(Kalkulyator):
    def __init__(self, uzunluq, en, hundurluk):
        super().__init__(uzunluq, en)
        self.hundurluk = hundurluk

    def hecm(self):
        return self.uzunluq*self.en*self.hundurluk
    
kvadrat = Kvadrat(3, 3)
kub = Kub(4, 4, 4)





print(kvadrat.sahe())
print(kub.hecm())