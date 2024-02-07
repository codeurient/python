# asctime() - ASCII time (ASCII-vaxti).

# Bu metod tuple() ve yaxud vaxt strukturu olan time.localtime() ve time.gmtime() qebul edir.
 
# tuple() icerisinde 9 deyer yazaraq asctime() metoduna parametr kimi gonderirik.

import time

vaxt_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)

# Bu metod hemin deyerleri vaxt-a cevirerek geri qaytarir
vaxt = time.asctime(vaxt_tuple)

print(vaxt)