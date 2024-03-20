
#! SELECT * FROM employeedb.employee2;

# INTERSECT - bir-biri ile kesişən deyerleri tapmaq ucun istifade edilir
# Yeni her iki setrde oolan ortaq setrleri qaytarir.

#! select FirstName, Department FROM employeedb.employee2
#! intersect
#! select FirstName, Department FROM employeedb.employee1;  


# Vacib qeyd: Bəzi verilənlər bazaları, xüsusilə MySQL, INTERSECT operatorunu dəstəkləmir. 
# Bu zaman eyni nəticəni INNER JOIN və ya digər üsullardan istifadə etməklə əldə etmək olar.