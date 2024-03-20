"""

SELECT FirstName, Occupation, EducationLevel, TotalChildren, sum(TotalChildren) 
over (partition by Occupation order by EducationLevel)  FROM expense.customers_data;



-- PARTITION BY Occupation o deməkdir ki, məlumatlar "Occupation" sütununun dəyərlerine əsasən qruplara bölünəcək.
-- ORDER BY EducationLevel o deməkdir ki, hər bir qrup daxilində dəyərlərin sıralaması EducationLevel sütununun dəyərlerine əsasən təyin edilsin.


"""