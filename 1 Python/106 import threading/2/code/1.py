import time

# Burda birinci 1. basla() sonra ise 2. sonlan() funksiyasi isleyir.
# Yeni, ikiside eyni vaxtda islemir. Sira ile isleyirler
# Ekrana string olaraq "başla" yazdirilir. Sonra sleep(3) metodu ile 3 saniye 
# yuxu moduna kecirik 3 saniye sonra ekrana "metn" stringi yazdirilir, arxasinca ise 
# sonlan() funksiyasi cagrilaraq "Son" stringi yazdirilir.
def basla():
    print("başla")
    time.sleep(3)
    print("metn")

def sonlan():
    print("Son")

basla()
sonlan()

#! Nece ede bilerik ki, basla() funksiyasi islemeye basladiqda onunla eyni vaxtda sonlan() funksiyasi da
#! cagrilaraq islesin.