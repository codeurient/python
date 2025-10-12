class Ordek():
    def gezmek(self):
        print("Bu ordek gezir")
    def danismaq(self):
        print("Bu ordek danisir")

class Toyuq:
    def gezmek(self):
        print("Bu toyuq gezir")
    def danismaq(self):
        print("Bu toyuq danisir")

class Adam:
    def tutmaq(self, qus):
        qus.gezmek()
        qus.danismaq()
        print("Siz heyvani tutdunuz")


ordek = Ordek()
toyuq = Toyuq()
adam = Adam()

adam.tutmaq(toyuq)