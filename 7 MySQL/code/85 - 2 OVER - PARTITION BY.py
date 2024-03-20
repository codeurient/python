"""

SELECT FirstName, Occupation, EducationLevel, TotalChildren, sum(TotalChildren) 
over (partition by Occupation) FROM expense.customers_data;


-- OVER xususi bir cercive yaradir (alan, sahe). Ve sum() metodu bu cercive daxilinde oz işini görür.alter
-- PARTITION BY kamandasi OVER kamandasinin bir paксasidir ve Occupation sutununa gore qruplasdir demek ucun istifade edilib. 	

-- Yəni, deyeri 'Clerical' olanlar bir, 'Management' bir sira ile qruplasacaqlar.


-- Bu qruplasma icerisinde de ORDER BY kamandasi ile siralama teyin ede bilerik. 

 """