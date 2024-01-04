class Ordek:
    def gezmek(self):
        print("Bu ordek gezir")
    def danismaq(self):
            print("Bu ordek danisir")

class Toyuq:
    def gezmek(self):
        print("Bu toyuq gezir")
    def danismaq(self):
        print("Bu toyuq danisir")

# 3 Class yaratdiq. 3cu class-in metodunun ikinci parametrine "ordek" adini verdik ki,
# hemin bu ucuncu klasin obyektini yaradaraq metodunu cagirdiqda, arqument kimi "Ordek"
# obyektini gonderek. #! Ancaq, burda "ordek" yazmagimiz sadece ordek klasinin obyektini
#! gondere bilerik menasina gelmir. Meselen, "Toyuq" obyektinide gondersek kod isleyecek.  
class Adam:
    def tutmaq(self, ordek):
        ordek.gezmek()
        ordek.danismaq()
        print("Siz heyvani tutdunuz")


ordek = Ordek()
toyuq = Toyuq()
adam = Adam()

#! Burda istesek "ordek"-de yaza bilerik "toyuq" da yaza bilerik. Kod yenede isleyecekdir. 
adam.tutmaq(ordek)