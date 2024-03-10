# difference_update() - Bu metod, birinci set-in icindeki elementleri ikinci set-in icinde olan elementler ile 
# yenileyerek birinci set-i qaytarir. Bu zaman movcud olan oxsar elementler silinecekdir.


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

# set1 update edilir set2 ile. Eyni olanlar silindi ferqli olanlar qaldi.
set1.difference_update(set2)
print(set1)  # {1, 2}





set3 = {1, 2, 3, 4}
set4 = {3, 4, 5}

# set4 update edilir set3 ile. Eyni olanlar silindi ferqli olanlar qaldi.
set4.difference_update(set3)
print(set3)  # {5}