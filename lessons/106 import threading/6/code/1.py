import time
import threading

def basla(a):
    print("başla")
    time.sleep(3)
    print(a + 5)

def sonlan():
    print("Son")

basla(3)
sonlan()

# Eger 1 dene parametr olarsa 1ci deyerden sonra mutleq vergul iwaresini qoymaq lazimdir:  "args=(2,)"
threading.Thread(target=basla, args=(2,)).start()
threading.Thread(target=sonlan).start()



