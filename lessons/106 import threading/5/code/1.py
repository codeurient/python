import time
import threading

def basla(a, b):
    print("başla")
    time.sleep(3)
    print(a + b)

def sonlan():
    print("Son")

# Thread() metodunun 2ci parametrine "args=()" deyerek, basla() funksiyasinin a ve b
# parametrlerine gonderilecek arqumentleri yaziriq.
threading.Thread(target=basla, args=(2, 3)).start()
threading.Thread(target=sonlan).start()