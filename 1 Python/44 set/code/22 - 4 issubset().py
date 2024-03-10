# set.issubset(basqa_set)

# issubset() - Bir set icinde olan elementler diger set icinde olan elemtler ile eynidirmi yoxlamaq ucun bu metoddan
# istifade edilir. 


# Bir dene ferqli deyer bele olarsa False qayidacaqdir. 1,2,3,4 var ancaq 9 yoxdur.
set1 = {1, 2, 3, 4, 9}
set2 = {1, 2, 3, 4, 5, 6, 7, 8}

# set1 varmi set2-nin icinde?
print(set1.issubset(set2))  # False         Butun deyerler movcud olmalidir ekse halda False qayidar.


# set2 varmi set1-in icinde?
print(set2.issubset(set1))  # False


#! Baxmiyaraq ki, set1 de olan elementler set2 de movcduddur, yenede 1 deyer (9) bele olmadigi ucun 
#! hec bir element bir-birinin ALT ELEMENTI deyildir. 
#! Ustunluk set2-dedir.