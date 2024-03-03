siyahi1 = [20, 30, 40, 50, 60, 70]

# 1ci olaraq kodun bu hissesi isleyir:   for i in siyahi1.         siyahi1-de olan deyerler 'i' adli variable-a gonderilir. 
# 2ci olaraq kodun bu hissesi isleyir:   if i > 45.                hemin 'i' variable-inda olan deyerler muqayise edilir.
# 3cu olaraq kodun bu hissesi isleyir:   i.                        Muqayiseden sonra deyerler en basdaki 'i' variable-a gonderilir.
# 4u  olaraq kodun bu hissesi isleyir:   siyahi3 =                 Basdaki  'i' variable-inda olan deyerler 'siyahi3'-e oturulur.
siyahi3 = [ i for i in siyahi1 if i > 45 ]
print(siyahi3)
