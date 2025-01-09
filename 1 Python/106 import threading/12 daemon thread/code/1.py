import time
import threading

def vaxt():
    say = 0
    while True:
        time.sleep(1)
        say += 1
        print("Sisteme daxil olma muddeti:", say, "saniye")

# daemon=True deyerek daemon thread-i işə salırıq.
x = threading.Thread(target=vaxt, daemon=True)
x.start()

# İndi terminalda bir seyler yazaraq yaxud yazmadan ENTER-e basdiqda proqram oz işini dayandiracaqdır.
cavab = input("Cixis etmek isteyirsinizmi?\n")