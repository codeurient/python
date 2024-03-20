"""


SELECT * FROM classicmodels.customers;

Delimiter &&
	create procedure get_credit(out deyisken int)
	begin
		select max(creditLimit) into deyisken from classicmodels.customers;
	end &&
Delimiter ;	


-- 1. maksimum deyeri tapmaqda istifade edilecek get_credit() adinda prosedura yaradiriq. 
-- 2. get_credit() proseduru tapdigi max deyeri 'deyisken' adli OUT parametri icine yazir.
-- 3. Prosedurlarin iş prinsipi 2 hisseden ibaretdir: a) YARADILMASI b) CAGRILMASI
-- 4. OUT acar sozu elde etdiyi deyeri YARADILAN prosedurdan CAGRILAN prosedura geri qaytarmaq ucun istifade edilir
-- 5. Yəni, max() metodu maksimum deyeri get_credit(out deyisken int) prosedurunda olan 'deyisken' parametrine verir
-- 6. OUT ise hemin deyeri 'call classicmodels.get_credit(@geriGeldi);' cagrilan prosedurun @geriGeldi deyiskenine oturur



set @geriGeldi = 0;
-- Prosedur yaradilanda daxil olan deyer OUT ile  cagrilan prosedura geri gonderilir.
call classicmodels.get_credit(@geriGeldi);
select @geriGeldi;

 

 """