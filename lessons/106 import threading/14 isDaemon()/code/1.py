import time
import threading

def vaxt():
    say = 0
    while True:
        time.sleep(1)
        say += 1
        print("Sisteme daxil olma muddeti:", say, "saniye")

x = threading.Thread(target=vaxt)
x.setDaemon(True)

x.start()

# daemon Thread-in aktiv olub olmadigini yoxlamaq ucun isDaemon() metodundan istifade edilir.
print(x.isDaemon())


cavab = input("Cixis etmek isteyirsinizmi?\n")