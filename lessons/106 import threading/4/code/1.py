import time
import threading

def basla():
    print("başla")
    time.sleep(3)
    print("metn")

def sonlan():
    print("Son")


#! Diqqet etdinizse funksiyanin adini yazdqiqda () yumru moterizeni yazmadiq.
#! Bele olan halda parametrleri olan funksiyalara arqument nece gondere bilerik ?
threading.Thread(target=basla).start()
threading.Thread(target=sonlan).start()