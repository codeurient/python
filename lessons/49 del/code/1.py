# set kolleksiyasinin ozunu silmek ucun del acar sozunden istifade edilir

# clear() metodundan istifade etdikde xeta almamisdiq.

# Ancaq del acar sozunden istifade etdikde xeta aliriq. Cunki sildikden sonra my_set adindan bir set 
# olmayacaq ve olmayan bir sey print etmek istedikde xeta alariq. 

my_set = {"alma", "armud", "nar"}

del my_set

print(my_set)