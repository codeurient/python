"""

SELECT FirstName, Occupation, EducationLevel, sum(TotalChildren) FROM expense.customers_data
group by FirstName, Occupation, EducationLevel; 


-- group by sadece qruplasdirmaq ucun istifade edilir. Ancaq hem qruplasdirmaq hemde siralamaq 
-- ucun OVER - PARTITION BY - ORDER BY kamandalarindan istifade ede bilerik. 

-- FirstName,Occupation ve EducationLevel sütunlarinin deyerleri eyni olanlari qruplasdirir ve TotalChildren cemini elde edirik
 

 """