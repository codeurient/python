# Eger her iki faylda oxunmaq ucun acilmiw olan eyni fayldirsa onda if eks halda else iwleyecekdir.


import os


yol1 = os.open('/Users/proj/domains/PYTHON/test.txt', os.O_RDONLY)
yol2 = os.open('/Users/proj/domains/PYTHON/test.txt',    os.O_WRONLY)


if os.path.sameopenfile(yol1, yol2):
    print("Eyni fayl")
else:
    print("Ferqli fayl")