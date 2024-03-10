# truncate() - bu metod faylin olcusunu azaltmaq yaxud artirmaq ucun istifade edilir.

# 1000 dedikde yeni 1000 byte nezerde tutulur. 


import os

yol = '/Users/proj/domains/PYTHON/test.txt'

olcu = 1000

os.truncate(yol, olcu)