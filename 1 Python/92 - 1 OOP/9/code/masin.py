# Xasselere verilen deyerleri istifade etmek ucun hemin xassenin adini 
# metodlara yazamaq mumkundur.

class Masin:

    def __init__(self, hazirlamaq, model, ili, rengi):
        self.hazirlamaq  = hazirlamaq
        self.model       = model
        self.ili         = ili
        self.rengi       = rengi

    def surmek(self):
        print(f"Masin {self.model} surulur")

    def dayanmaq(self):
        print(f"Masin {self.model} dayandi")

    


