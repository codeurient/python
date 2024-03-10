from abc import ABC, abstractmethod

class NeqliyyatVasitesi(ABC):
    @abstractmethod
    def getmek(self):
        pass

class Masin(NeqliyyatVasitesi):
    def getmek(self):
        print("Sen masin surursen")

class Motosiklet(NeqliyyatVasitesi):
    def getmek(self):
        print("Sen motosiklet surursen")
#! sildik 
masin = Masin()
motosiklet = Motosiklet()
#! sildik 
masin.getmek()
motosiklet.getmek()
