"""



SELECT * FROM classicmodels.customers;

Delimiter &&
	create procedure get_limit(in deyisken int)
	begin
		select * from classicmodels.customers LIMIT deyisken;
	end &&
Delimiter ;	

 

 """