import time

def saymaq(eded):
    say = 0
    while say < eded:
        say += 1

def esas(eded1, eded2, eded3, eded4):

    baslama_vaxti = time.perf_counter()

    # saymaq() funksiyasi 1 defe cagrildiqda texmini icra muddeti 3s-dir 
    # saymaq() funksiyasi 2 defe cagrildiqda texmini icra muddeti 6s olur. 
    #! Yəni, hər funksiya eyni vaxtda paralel şəkildə yox ayrı-ayrı sıra ilə işləyir.
    #! multiprocessing bunun üçün lazımdır ki, birdən çox işi eyni vaxtda görə bilək.
    saymaq(eded1)
    saymaq(eded2)

    bitme_vaxti = time.perf_counter()
    icra_muddeti = bitme_vaxti - baslama_vaxti

    print("finished in:", icra_muddeti, "seconds")


if __name__ == '__main__':
    esas(125000000,125000000,125000000,125000000)