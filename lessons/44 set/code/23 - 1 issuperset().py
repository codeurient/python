# set.issuperset(basqa_set)

# issuperset() - Bir set icinde olan elementler diger set icinde olan elemtler ile eynidirmi yoxlamaq ucun bu metoddan
# istifade edilir. 


# Muqayise vaxti, butun elementler movcud olarsa True eks halda False qayidir. 
set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3, 4}


# set1-in icinde set2 varmi?
print(set1.issuperset(set2))  # True      


# set2-in icinde set1 varmi?
print(set2.issuperset(set1))  # False


#! Bu misallarda cox olan az olanin UST ELEMENTIDIR... Yeni set2-nin UST ELEMENTI set1-dir.