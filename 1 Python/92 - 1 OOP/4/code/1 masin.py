# __init__() - bu metod klasin konstruktorudur. Ve Klasin obyektini yaratdigimiz zaman
# hemin bu metod avtomatik olaraq cagrilacaqdir. 

# Yeni normalda funksiyani cagirmaq ucun adini yazmaq lazimdir. Burda ise __init__() metodunu
# cagirmaq ucun klasin obyektini yaratmaq lazimdir. Klasin obyektini yaratdiqda hemin bu metod
# avtomatik olaraq cagrilacaqdir.

class Masin:

    def __init__(self, hazirlamaq, model, ili, rengi):
        # self.model deyerek xasse yaratdiriq ve her xasseye bir parametr teyin edirik.
        self.hazirlamaq  = hazirlamaq
        self.model       = model
        self.ili         = ili
        self.rengi       = rengi

    def surmek(self):
        print("Masin surulur")

    def dayanmaq(self):
        print("Masin dayandi")