from abc import ABC, abstractmethod

class NeqliyyatVasitesi(ABC):
    @abstractmethod
    def getmek(self):
        pass

class Masin(NeqliyyatVasitesi):
    def getmek(self):
        print("Sen masin surursen")

class Motosiklet(NeqliyyatVasitesi):
#! Eger subklas ana klasi izleyirse ve ana klas abstract olarsa, onda hemin subclass
#! ana klasin metodunu mutleq ozunde gostermelidir. Eks halda xeta alariq.
    pass

masin = Masin()
motosiklet = Motosiklet()

masin.getmek()
