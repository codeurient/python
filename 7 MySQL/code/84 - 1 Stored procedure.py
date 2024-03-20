"""

-- Stored procedure (Saxlanılan prosedur) nedir ? Saxlanilan dedikde yeni harasa hek olunmus yeni harasa yaddasa yazilmis emeliyyat, prosedur.
-- Daha etrafli desek SQL dilinde bir kod yaziriq ve hemin kodu yadda saxlayiriq ki, gelecekde yeniden yazmayaq. Istenilen vaxt cagiraq ve istifade edek, 
-- yaxud deyisdirek ve.s

# SQL dilinde yazilan kodlara SQL kamandalari deyilir. Ferqli SQL komandalari birleserek bir butun komanda emele getirir.
# Oxunmasi rahat olsun deye 1 butun olan kamandani emele getiren kicik kamandalar alt-alta yeni setrlerden yazila biler.
# Bir butun olan bu komanda sonlandigi zaman noqteli vergulden istifade edilir. Yəni, hemin komandanin en sonunda ; simvolu qoyulur.
# Eger 1 butun komandani emele getiren her kicik kamandadan sonra ; simvolu qoyarsaq onda xeta alariq. 
# SQL -de diqqet edilmesi gereken bezi nuanslar vardir. Meselen, bunlardan biri komandalarin SELECT ile ve SELECT olmadan istifade edilmesidir.
# SELECT ile istifade edildikde ferqli komandalar bele olsalar SELECT icinde olduqlari ucun bu BIR komanda sayilir ve noqteli vergul sonda qoyulur.

# Birde proqramlasdirma dillerinde oldugu kimi yazilan kod tipli kamandalar vardir. Bunlarin her birini ise noqteli vergul ile ayirmaq lazimdir.
# Ancaq her ayri kod parcalari noqteli vergul ile ayrildiqda SQL xeta kimi qebul edir bu noqteli vergulu. Bunun ucun hemin SIMVOLU (;) nezere almamaq ucun
# Delimiter (Mehdudlasdirici) emrinden istifade edilmelidir. Eks halda xeta alariq. Delimiter muveqqeti olaraq ; simvolunu // simvolu ile evez edir.
# // bu simvol evezine && bele bir simvolda yaza bilerdiniz.  Yəni, DELIMITER -den sonra yazilan simvol sadece noqteli vergulu evez etmek ucun istifade edilen 
# muveqqeti simvoldur. En sonda yeniden DELIMITER ; yazaraq // yaxud && simvollarini ; ile evez edirik. 	
 
 
# DOGRU 
-- SELECT * FROM demo1.emp_data 
-- WHERE NOT (`Job Title` = "Sr. Manger" OR City = 'Seattle');


# YANLIS 
-- SELECT * FROM demo1.emp_data; 
-- WHERE NOT (`Job Title` = "Sr. Manger" OR City = 'Seattle');


# Ardi var ....

"""