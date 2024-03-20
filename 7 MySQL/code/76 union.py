
#! SELECT * FROM employeedb.employee2;

# UNION iki və ya daha çox SELECT ifadəsinin nəticələrini vahid nəticə dəstində birləşdirmək üçün istifadə olunur. 
# Varsayılan olaraq, dublikat deyerleri silir. 

# NOT! Diqqət yetirməli vacib məqam odur ki, UNION-da bütün SELECT ifadələrində sütunların sayı və onların növləri (tipleri) bir-birine uyğun gelmelidir.
# Eks halda xeta ala bilerik. 

#! SELECT FirstName, Department FROM employeedb.employee2
#! union
#! SELECT FirstName, Department FROM employeedb.employee1;


# 7 (setr) + 7 (setr) = 14 - 3 (oxsarlar) = 11