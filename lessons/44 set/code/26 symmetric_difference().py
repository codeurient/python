# symmetric_difference() - Bu metod, birinci set-in icindeki elementleri ikinci set-in icinde olan elementler ile 
# muqayise ederek yeni set qaytarir. Bu zaman movcud olan oxsar elementler yox oxsar olmayan elementler qayidacaqdir.


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

# set1 muqayise edilir set2 ile.  Eyni olanlar silindi ferqli olanlar qayitdi.
yeni_set = set1.symmetric_difference(set2)
print(yeni_set)  # {1, 2, 5}





set3 = {1, 2, 3, 4}
set4 = {3, 4, 5}

# set1 update edilir set2 ile.  Eyni olanlar silindi ferqli olanlar qayitdi.
yeni_set = set4.symmetric_difference(set3)
print(yeni_set)  # {1, 2, 5}