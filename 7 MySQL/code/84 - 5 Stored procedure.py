"""



SELECT * FROM classicmodels.customers;

# Bu kod asagida yazdigimiz prosedura ile eyni isi gorur.
# Loru sekilde desek manual olan isi avtomatlasdirmis olduq.
-- SELECT * FROM customers WHERE city IN ('Nantes');


Delimiter &&
	create procedure get_limit(in deyisken VARCHAR(255))
	begin
		select * from classicmodels.customers WHERE city = deyisken;
	end &&
Delimiter ;	


-- call classicmodels.get_limit('Nantes'); - diger terefde kod bele gorsenir.

 

 """