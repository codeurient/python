
#! SELECT * FROM classicmodels.products;

# case - veziyyete, hala gore ne etmek lazim oldugunu teyin edir.
# Şərti ifadələri qiymətləndirmək və müəyyən bir şərt əsasında müxtəlif nəticələr çıxarmaq üçün istifadə olunur.
#! select productName, quantityInStock,

#! case
#! 	when quantityInStock < 1000 then "təcili daha çox ehtiyat lazımdır"
#!     else "hal-hazırda heç bir tələb yoxdur"
#! end as production_details

#! from classicmodels.products;