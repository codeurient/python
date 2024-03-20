# Eger NOT komandinin her iki terefe aid olmasini isteyirikse onda () morterizeden istifade etmeliyik


# SELECT * FROM demo1.emp_data WHERE NOT (`Job Title` = "Sr. Manger" AND City = 'Seattle');


# Eyni vaxt da `Job Title` = "Sr. Manger" VE City = 'Seattle' olmayan deyerler hansilardisa onlari elde edirik.
# Eger `Job Title` = "Sr. Manger" VE City = 'Seattle' olan setr olarsa onda NOT yeni YOX yeni elde etme demis oluruq.



# Demeli, burda   `Job Title` = "Sr. Manger" olanlari elde edirik     VE     City = 'Seattle' olanlari ede edirik
#! ANCAQ bir setrde hem  "Sr. Manger" hemde 'Seattle' lan sutunlar hansidirsa onlari elde etmirik.



# EGER hec birini elde etmek istemirikse onda AND evezine OR istifade etmeliyik. SEKIL 33 - 3.png