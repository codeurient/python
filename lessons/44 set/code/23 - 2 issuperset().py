# set.issuperset(basqa_set)

# issuperset() - Bir set icinde olan elementler diger set icinde olan elemtler ile eynidirmi yoxlamaq ucun bu metoddan
# istifade edilir. 


# Iki set-de olan deyerler eyni ve beraber olarsa her ikisi True qaytaracaqdir.
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4}

# set1-in icinde set2 varmi?
print(set1.issuperset(set2))  # True

# set2-in icinde set1 varmi?
print(set2.issuperset(set1))  # True



#! Her iki elementde eyni deyerlere sahib oldugu ucun her iki element bir-birinin UST ELEMENTIDIR. 
