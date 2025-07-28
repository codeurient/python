# Ilk once tekrarlanan kodlari subclass-lardan aliriq ve ana klasa veririk.

#! Sonra ise super() adli funksiyamizdan istifade ederek, ana klasa muraciet edirik.

# super() - bu funksiya subclass icinde istifade edildikde, avtomatik olaraq hemin 
# subclass-in ana klasina muraciet edir. 

#! super().__init()__ onu bildirir ki, biz ana klasin __init__() konstruktorunu cagiririq.

class Kakulyator:
    def __init__(self, uzunluq, en):
        self.uzunluq = uzunluq
        self.en = en

class Kvadrat(Kakulyator):
     def __init__(self, uzunluq, en):
        super().__init__(uzunluq, en)

class Kub(Kakulyator):
    def __init__(self, uzunluq, en, hundurluk):
        super().__init__(uzunluq, en)
        self.hundurluk = hundurluk

kvadrat = Kvadrat(3, 3)
kub = Kub(3, 3, 3)