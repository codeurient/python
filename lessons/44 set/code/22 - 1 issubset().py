# set.issubset(basqa_set)

# issubset() - Bir set icinde olan elementler diger set icinde olan elemtler ile eynidirmi yoxlamaq ucun bu metoddan
# istifade edilir. 


# Muqayise vaxti, butun elementler movcud olarsa True eks halda False qayidir. 
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5, 6}

# set1 varmi set2-nin icinde?
print(set1.issubset(set2))  # True      


# set2 varmi set1-in icinde?
print(set2.issubset(set1))  # False


#! Bu misallarda az olan cox olanin ALT ELEMENTIDIR... Yeni set2-nin ALT ELEMENTI set1-dir.
#! Ustunluk set2-dedir.