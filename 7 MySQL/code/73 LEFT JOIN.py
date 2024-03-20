
#! SELECT * FROM classicmodels.products;

# LEFT JOIN sol cədvəl və sağ cədvəl arasındakı əlaqə əsasında birləşmə həyata keçirir. 
# Sol cədvəldəki bütün dəyərlər sağ cədvəldəki uyğun dəyərlərlə birlikdə götürülür.  (Burda SOL cedvel products olacaqdir. Yəni, esas cedvel SOL cedveldir.)
# Sağ cədvəldə uyğun gəlməyən sətirlər üçün sol cədvəlin dəyərləri alınır və sağ cədvələ NULL dəyərlər təyin edilir.

#! SELECT products.productName, `order details`.quantityOrdered

#! 	FROM classicmodels.products 
    
#!  LEFT JOIN classicmodels.`order details` 
    
#! 	ON products.productCode = `order details`.productCode;


# left join yeni A da olan butun deyerler ve A ile B -nin ortax deyerleri.