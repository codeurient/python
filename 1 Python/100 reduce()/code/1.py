# reduce() metodunu istifade ede bilmek ucun "functools" modulunu import edirik.
import functools

# list yaradiriq.
ededler = [1, 2, 3, 4, 5]

# reduce() metodunun 3 parametri olur. 
#! reduce(function, iterable, initializer=None)
#? 1. function - her zaman 2 parametr qebul edir: func(accumulator, element)
    # a) element     - iterable object-den gelen deyerler ilk once bu parametr icine gelir sonra accumulator-a gonderilir.
    # b) accumulator - ikinci parametr-de yigilan deyerler bir-bir bu paramtr icine gelir. 
#? 2. iterable - tekrarlana bilen obyekt. Bu obyektin icinden goturulur deyerler.
#? 3. initializer=None - mutleq olmayan parametr. Eger meselen 5 yazsaq bu o demekdir ki, baslangic deyer 5 olacaq.

# Yoxlamaq ucun 1ci print edirik "x" parametrini sonra ise "y".
# x: 1,  y: 2
# x: 3,  y: 3
# x: 6,  y: 4
# x: 10, y: 5
# Final netice: 15+5 = 20
final_netice = functools.reduce(lambda x, y: x + y, ededler, 5)
print(final_netice)