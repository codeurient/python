# intersection_update() - Bu metod, birinci set-in icindeki elementleri ikinci set-in icinde olan elementler ile 
# yenileyerek birinci set-i qaytarir. Bu zaman movcud olan oxsar olan elementler qalacaqdir.


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

# set1 update edilir set2 ile.  Eyni olanlar qladi ferqli olanlar silindi.
set1.intersection_update(set2)
print(set1)  # {3, 4}





set3 = {1, 2, 3, 4}
set4 = {3, 4, 5}

# set4 update edilir set3 ile.  Eyni olanlar qladi ferqli olanlar silindi.
set4.intersection_update(set3)
print(set4)  # {3, 4}