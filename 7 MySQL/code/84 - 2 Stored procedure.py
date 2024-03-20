"""

-- Prosedurla yaratmaq ucun CREATE PROCEDURE kamandasindan istifade edilir sonra ise bu proseduraya ad vermek lazimdir.
-- Proseduralari proqramlasdirma dilinde ki, funksiyalar kimi qebul etmek olar.
 
 
 

# DOGRU
DELIMITER //
	CREATE PROCEDURE tekrarla (id1 INT)
	BEGIN
		DECLARE x INT;
		SET x = 0;
		REPEAT SET x = x + 1; UNTIL x > id1 END REPEAT;
		SET @x = x;
	END //
DELIMITER ;



 
# XETALI 
CREATE PROCEDURE tekrarla (id1 INT)
BEGIN
    DECLARE x INT;
    SET x = 0;
    REPEAT SET x = x + 1; UNTIL x > id1 END REPEAT;
    SET @x = x;
END //

 
 

 """