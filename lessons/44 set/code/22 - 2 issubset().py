# set.issubset(basqa_set)

# issubset() - Bir set icinde olan elementler diger set icinde olan elemtler ile eynidirmi yoxlamaq ucun bu metoddan
# istifade edilir. 


# Iki set-de olan deyerler eyni ve beraber olarsa her ikisi True qaytaracaqdir.
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4}

# set1 varmi set2-nin icinde?
print(set1.issubset(set2))  # True

# set2 varmi set1-in icinde?
print(set2.issubset(set1))  # True



#! Her iki elementde eyni deyerlere sahib oldugu ucun her iki element bir-birinin ALT ELEMENTIDIR. 
#! Ustunluk set2-dedir.