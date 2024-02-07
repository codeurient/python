# active_count() - aktiv thread-lerin sayini elde etmek ucun istifade edilen metoddur.

import time
import threading

def basla(a):
    print("başla")
    time.sleep(3)
    print(a + 5)

def sonlan():
    print("Son")

threading.Thread(target=basla, args=(2,)).start()
threading.Thread(target=sonlan).start()


print(   threading.active_count()   )