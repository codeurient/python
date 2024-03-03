# symmetric_difference_update() - Bu metod, birinci set-in icindeki elementleri ikinci set-in icinde olan elementler ile 
# yenileyir. 


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

# set1 muqayise edilir set2 ile.  Eyni olanlar silindi ferqli olanlar qayitdi.
# Bu metod movcud variable uzerinde deyisiklik edir ve symmetric_difference() metodunda oldugu kimi 
# yenisini yaratmagi teleb etmir.
set1.symmetric_difference_update(set2)
print(set1)  # {1, 2, 5}







set3 = {1, 2, 3, 4}
set4 = {3, 4, 5}

# set4 muqayise edilir set3 ile.  Eyni olanlar silindi ferqli olanlar qayitdi.
# Bu metod movcud variable uzerinde deyisiklik edir ve symmetric_difference() metodunda oldugu kimi 
# yenisini yaratmagi teleb etmir.
set4.symmetric_difference_update(set3)
print(set4)  # {1, 2, 5}