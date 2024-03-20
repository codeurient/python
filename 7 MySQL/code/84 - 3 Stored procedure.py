"""



-- Gelin indi bu kodu oxuyaq. 
-- 1. DELIMITER -in ne oldugunu artiq bilirik.
-- 2. CREATE PROCEDURE -un ne oldugunu artiq bilirik.

DELIMITER //

	--  tekrarla() bizim Saxlanmis Proseduramizin adidir. 
    -- id1 INT hemin Saxlanmis Proseduranin parametridir. Bu proseduru cagirdiqda ona deyer vereceyik ve hemin deyeri bu 'id1' parametri qebul edecek.
	CREATE PROCEDURE tekrarla (deyer INT)
    
    -- BEGIN ve END Prosedura kodlarini yazmagimiz ucun bloku emele getiren acar sozlerdir. Kodlar blok icinde yazilir.
	BEGIN
    -- DECLARE local deyisken yeni local variable yaratmaq ucun istifade edilen acar sozdur. Hemin deyiskenin onunde yazilan 
    -- INT bu deyiskenin tipini teyin edir. Yeni reqemsaldir.
		DECLARE eded INT;
        
        -- SET yaradilan deyiskene (variable-a) deyer vermek ucun istifade edilen EMR kamandasidir-dir. 
        -- SET yazmadan deyer vermekde mumkundur. Bunun ucun ise := operatorundan istifade etmeliyik.  x := 10;
        -- SET ile LOCAL deyiskeni cagirmaq yaxud SESSIYA deyiskeni yaratmaq ucun istifade edilir.
		SET eded = 0;
        
	
        -- 2. REPEAT SET ifadəsi müəyyən bir şərt yerinə yetirilənə qədər əməliyyatı təkrarlamaq üçün istifadə olunur.
		REPEAT SET eded = eded + 1; 
            
		-- 1. UNTIL ifadəsi şərt qoşmaq üçün istifade edilir.
		UNTIL eded > deyer END REPEAT;
        
        -- Burada SET emri SESSIA deyiskeni yaratmaq ucun istifade edilir ve sessiya deyiskenleri qarsisinda @ simvolu yazilir.
        -- Sessiya deyiskenlerine GLOBAL deyiskenlerde demek olar. Kodun istenilen yerinde istifade etmemiz ucun gereklidir.
        -- @eded basqa deyiskendir eded basqa deyiskendir yeni eyni deyildirler. local eded variable-inin deyerini global @eded variable-ina veririk.
		SET @eded = eded;
	END //
    
DELIMITER ;
# Proqrami ise salaraq prosedurani basladiriq. Bir deyer girmeyimiz teleb edilecekdir. Girilen deyer tekrarla() prosedurasinin 'deyer' adli 
# parametrine gonderilir. Hemin deyer adli parametrde olan ededi ekrana yazdirmaq ucun SELECT kamandindan istifade edirik: SELECT @eded;



 

 """