
#! SELECT * FROM classicmodels.products;

# RIGHT JOIN sag cədvəl və sol cədvəl arasındakı əlaqə əsasında birləşmə həyata keçirir. 
# Sag cədvəldəki bütün dəyərlər sol cədvəldəki uyğun dəyərlərlə birlikdə götürülür.  (Burda SAG cedvel `order details` olacaqdir. Yəni, esas cedvel SAG cedveldir.)
# Sag cədvəldə uyğun gəlməyən məlumatlar varsa, sol cədvəldə olan məlumatlar göstəriləcək və digər sütunlar üçün NULL dəyərlər olacaq.

#! SELECT products.productName, `order details`.quantityOrdered

#! 	FROM classicmodels.products 
    
#!     RIGHT JOIN classicmodels.`order details` 
    
#! 	ON products.productCode = `order details`.productCode;
    
# SAG cedveldeki butun deyerler ve SAG cedvel ile SOL cedveldeki ortaq deyerler. Meselen:
# productCode: S18_1749, S18_2248, S18_4409 var ve bu product kodlara uygun gelen productName-ler var.
# Ancaq productCode: S24_3969 -a uygun gelen productName olmadigi ucun SAG cedvel oldugu kimi yazilir, Yeni 49 yazilir ancaq qabagina NULL qeyd edilir.
    
