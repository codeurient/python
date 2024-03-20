"""

SELECT * FROM classicmodels.customers;

Delimiter &&
	create procedure get_name(inout eded int)
	begin
		select customerName from customers where customerNumber = eded ;
	end &&
Delimiter ;	

-- inout hem giris melumatlarini hemde cixis melumatlarini elde etmek ucun istifade edile biler.
-- Yeni 2 cur istifade edile biler

-- 1. Bele yazildiqda netice olaraq verir: 'Havel & Zbyszek Co'
set @eded = 125;
call classicmodels.get_name(@eded);


-- 2. Bele yazildiqda netice olaraq verir: 125
-- set @eded = 125;
-- call classicmodels.get_name(@eded);alter
-- select @eded;

 

 """