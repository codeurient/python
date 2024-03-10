# set.issubset(basqa_set)

# issubset() - Bir set icinde olan elementler diger set icinde olan elemtler ile eynidirmi yoxlamaq ucun bu metoddan
# istifade edilir. 


# Iki set-de olan deyerler eyni olmaz ise onda her iki set-de False qaytaracaqdir.
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}

# set1 varmi set2-nin icinde?
print(set1.issubset(set2))  # False


# set2 varmi set1-nin icinde?
print(set2.issubset(set1))  # False




#! Her iki elementde ferqli deyerlere sahib oldugu ucun her iki element bir-birinin ALT ELEMENTI deyil. 
#! Ustunluk set2-dedir.