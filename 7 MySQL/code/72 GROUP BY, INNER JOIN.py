# SELECT * FROM classicmodels.products;



# SELECT products.productName, sum(`order details`.quantityOrdered)
# 	FROM classicmodels.products 
# 		INNER JOIN classicmodels.`order details` 					
# 			ON products.productCode = `order details`.productCode
#             GROUP BY products.productName


			
# Ferqli tarixlerde eyni maldan ferqli kemiyyetlerde sifaris edilmis ola biler. 
# Eger eyni adda olan maldan umumilikde ne qeder sifaris edildiyini oyrenmek isteyirikse onda
# hemin mal adlarini qruplasdirmaliyiq ve sum() funksiyasi ile cemlemeliyik.