
#! SELECT * FROM classicmodels.products;

# 2 ferqli cedvel bir-brine 'productCode' ile baglidir. 
# productName adindaki maldan neçə eded (quantityOrdered) sifaris edildiyini oyrenmek ucun 2 cedveli birlesdiririk. 
# Hemin 2 cedeveli birlesdirmek ucun 'productCode' ile onlari muqayise edirik. 
# Cedvelleri birlesdirdikde onlarin Verilenler bazasinin adinida qeyd etmek lazimdir.

#! SELECT products.productName, sum(`order details`.quantityOrdered)
	#! FROM classicmodels.products 
		#! INNER JOIN classicmodels.`order details` 					
            # INNER JOIN  cedvelleri birlesdirmek ucun istifade edilen komandadir.
			#! ON products.productCode = `order details`.productCode; 
            # ON 2 cədvəli birləşdirmək üçün istifadə olunan uyğunluq vəziyyətini təyin edir. 
            # ON ilə müəyyən edilmiş şərt hər iki cədvəldə sütunlar arasında əlaqəni müəyyən edir.
