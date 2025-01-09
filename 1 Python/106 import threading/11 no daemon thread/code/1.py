# daemon thread - seytan thread

# thread-ler hem ön hem arxa rejimde işleyirler.

# daemon thread arxa rejimde iş goren thread-lere deyilir.

# daemon thread-ler ancaq Ön rejimde thread işlediyi müddətcə işləyə bilər.

# Ön rejimde işləyən thread işini dayandırdıqda daemon thread-lərdə avtomatik olaraq öz işini dayandıracaqdır.

#? Bu numune 'daemon thread' olmadan gosterilen numunedir. 
import time
import threading

# funksiya variable yaradir ve sonsuz dongu her 1 saniye-den sonra "say" variable-inin deyerini 
# bir-bir artirir.
def vaxt():
    say = 0
    while True:
        time.sleep(1)
        say += 1
        print("Sisteme daxil olma muddeti:", say, "saniye")

x = threading.Thread(target=vaxt)
x.start()

# Terminal pencerede yazi yazaraq ENTER desek bele proqram öz işini dayandırmayacaqdır.
# Bes nece etmek olar ?
cavab = input("Cixis etmek isteyirsinizmi?\n")