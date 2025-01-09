import time
import threading

def vaxt():
    say = 0
    while True:
        time.sleep(1)
        say += 1
        print("Sisteme daxil olma muddeti:", say, "saniye")

x = threading.Thread(target=vaxt)

# Python-inin kohne versiyalarinda "daemon=True" parametri olmadigi ucun daemon Thread 
# yaratmaq ucun setDaemon(True) metodundan istifade edilirdi.
x.setDaemon(True)

x.start()

cavab = input("Cixis etmek isteyirsinizmi?\n")