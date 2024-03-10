# Neye lazimdir axi bu ana klas ve subclass? Eger ana klas olmasa idi, hemin bu 
# ana klasda yazilan kodlari tekrar-tekrar ayriliqda subclass-lar ucun yazmali olardiq.

# Eger indi yatmaq() metodunu dinlenmek() metodu ile evez etmek istesek, gerek her
# klass ucun ayri-ayri deyisiklik edek ve bu artiq vaxt itkisi demekdir.
class Dovsan():
    canli = True

    def yemek(self):
        print("Bu heyvan yemek yeyir")

    def dinlenmek(self):
        print("Bu heyvan yatir")

class Baliq():
    canli = True

    def yemek(self):
        print("Bu heyvan yemek yeyir")

    def dinlenmek(self):
        print("Bu heyvan yatir")

class Sahin():
    canli = True

    def yemek(self):
        print("Bu heyvan yemek yeyir")

    def dinlenmek(self):
        print("Bu heyvan yatir")

dovsan = Dovsan()
baliq  = Baliq()
sahin  = Sahin()