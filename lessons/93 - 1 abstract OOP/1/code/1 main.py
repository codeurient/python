# abstract class - Bir yaxud birden cox abstract metodu olan klasslara deyilir.

# abstract class yaratmaq ucun "abc" modulundan istifade edilir.

# abstract metod ana klasda yaradildiqda bu o menaya gelir ki, hemin ana klasi 
# izleyen subclass mutleq sekilde hemin ana klasin abstract metodunu istifade etsin.

# abstract klasin govdesi olmur. Bunun ucun pass acar sozunden istifade edirik.

from abc import ABC, abstractmethod
#! abstract klas ve abstract metod
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

#! abstrac klas-in obyektini yaratmaq olmur: xeta
neqliyyatVasitesi = NeqliyyatVasitesi()
masin = Masin()
motosiklet = Motosiklet()

#! abstrac klas-in metodunu cagirmaq olmur: xeta
neqliyyatVasitesi.getmek()
masin.getmek()
motosiklet.getmek()
