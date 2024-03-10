# set.issuperset(basqa_set)

# issuperset() - Bir set icinde olan elementler diger set icinde olan elemtler ile eynidirmi yoxlamaq ucun bu metoddan
# istifade edilir. 


# Bir dene ferqli deyer bele olarsa False qayidacaqdir. 1,2,3,4 var ancaq 9 yoxdur.
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {1, 2, 3, 4, 9}

# set1-in icinde set2 varmi?
print(set1.issuperset(set2))  # False         Butun deyerler movcud olmalidir ekse halda False qayidar.


# set2-in icinde set1 varmi?
print(set2.issuperset(set1))  # False


#! Baxmiyaraq ki, set2 de olan elementler set1 de movcduddur, yenede 1 deyer (9) bele olmadigi ucun 
#! hec bir element bir-birinin UST ELEMENTI deyildir.