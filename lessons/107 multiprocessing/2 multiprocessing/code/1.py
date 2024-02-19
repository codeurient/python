from multiprocessing import Process, cpu_count
import time

def saymaq(eded):
    say = 0
    while say < eded:
        say += 1

def esas():
    # cpu_count() - bu metod komputerde olan CPU-nun neçə nüvəli olduğunu öyrənmək üçündür.
    print(cpu_count())
    baslama_vaxti = time.perf_counter()
    # Process() - bu metoddan yeni process (əməliyyat, iş) yaratmaq üçün istifadə edilir.
    # Hal-hazırda 2 ferqli əməliyyat paralel şəkildə işləyir. Əməliyyatın təxmini icra müddəti 3 saniyədir.
    #! Eger multiprocessing-den istifade etmese idik, onda hər cagrilan funksiya ayri-ayri 3 saniye erzinde icra olunacaqdı.
    #! Bu da ümumilikdə 6 saniyə edir.
    a = Process(target=saymaq, args=(125000000,))
    b = Process(target=saymaq, args=(125000000,))

    a.start()
    b.start()

    # join() metodu ne edir? Yuxarıda yazdigimiz kod oz isini tamamlamadan asagidaki kod işləməyə başlamasın. 
    # Yəni yuxarıdakı prosesin bitməsini gözləmək üçün join() metodundan istifade edilir.
    a.join()
    b.join()

    bitme_vaxti = time.perf_counter()
    icra_muddeti = bitme_vaxti - baslama_vaxti

    print("finished in:", icra_muddeti, "seconds")

if __name__ == '__main__':
    esas()