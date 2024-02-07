import time
import threading

def basla():
    print("başla")
    time.sleep(3)
    print("metn")

def sonlan():
    print("Son")


#! basla() funksiyasi islemeye basladiqda onunla eyni vaxtda sonlan() funksiyasi da cagrilaraq
#! hem "başla" hem "Son" string-leri ekrana yazdirilir.
threading.Thread(target=basla).start()
threading.Thread(target=sonlan).start()