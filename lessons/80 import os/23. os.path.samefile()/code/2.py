# Eger gosterilen yol ile yaradilan simvolik link eynidirse onda if
# ekse halda else iwleyecekdir.

import os

yol1 = '/Users/proj/domains/PYTHON/example.txt' 

os.symlink(yol1, 'yeniFayl.txt')

yeni_simvolik_link = '/Users/proj/domains/PYTHON/yeniFayl.txt'

if os.path.samefile(yol1, yeni_simvolik_link):
    print("Eyni fayl")
else:
    print("Ferqli fayl")