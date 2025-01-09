# Kodlar yuxardan asagiya dogru sira ile oxunur.

import threading
import time

def join_olmadan_tapsiriq():
    print("Bu tapsiriq join olmadan isledi")
    time.sleep(5)
    print("join olmayan tapsiriq basa catdi")

join_olmadan = threading.Thread(target=join_olmadan_tapsiriq)
#! Burda THREAD isledikde ekrana print() metodu icinde olan Stringler eyni vaxtda yazdirilir:
    #! a)  print("Bu tapsiriq join olmadan isledi")
    #! b)  print("Bu kod Thread-in basa catmasini gozlemeden isledi.")
join_olmadan.start()

print("Bu kod Thread-in basa catmasini gozlemeden isledi.")

#! join() metodundan istifade etdikde ise: 
    #! a) 1ci print("Bu tapsiriq join olmadan isledi") - ekrana yazdirilir
    #! b) 2ci time.sleep(5) - 5 saniye bitene qeder gozlenilir 

    #! c) 3cu print("join olmayan tapsiriq basa catdi") ve print("Bu kod Thread-in basa catmasini gozlemeden isledi.") - eyni vaxtda yazdirilir.

# Yeni join() metodu varsa eger, Thread-in basa catmasini gozlemek lazimdir.
# Eger join() metodu yoxdursa, onda Thread-in basa catmasini gozlemek lazim deyil.