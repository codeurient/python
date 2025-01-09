# Vaxt ile islemek ucun time modulunu import etmeliyik.
import time

# ctime() - current time - hal hazirki vaxti elde etmek ucun istifade edilir.

# parametr olaraq 0 sifir yazdiqda, epoxa elde edirik. EPOXA nedir ? Epoxa vaxtin bawlangicidir. 
# Python-da ise vaxtin bawlangici olara qebul edilen tarix beledir: #! Thu Jan  1 04:00:00 1970
print(   time.ctime(0)   )