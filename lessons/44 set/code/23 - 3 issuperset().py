# set.issuperset(basqa_set)

# issuperset() - Bir set icinde olan elementler diger set icinde olan elemtler ile eynidirmi yoxlamaq ucun bu metoddan
# istifade edilir. 


# Iki set-de olan deyerler eyni olmaz ise onda her iki set-de False qaytaracaqdir.
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}

# set1-in icinde set2 varmi?
print(set1.issuperset(set2))  # False


# set1-in icinde set2 varmi?
print(set2.issuperset(set1))  # False




#! Her iki elementde ferqli deyerlere sahib oldugu ucun her iki element bir-birinin UST ELEMENTI deyil. 
