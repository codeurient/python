
# set.isdisjoint(basqa_set)

# isdisjoint() - iki ferqli set-in ortaq elementlərinin olub olmadığını müəyyən etmək üçün istifadə olunur. Əgər set-lerin 
# ümumi elementləri yoxdursa, metod True, əks halda isə False qaytarır.

set1 = {1, 2, 3}

set2 = {4, 5, 6}
set3 = {3, 4, 5}



print(set1.isdisjoint(set2))  # True, ortaq elementleri yoxdur


print(set1.isdisjoint(set3))  # False, ortaq elementleri var. Hemin ortaq element 3 ededirir.