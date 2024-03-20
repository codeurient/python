"""

SELECT FirstName, SUM(TotalChildren) FROM expense.customers_data 
WHERE FirstName = 'ALEXIS' AND Occupation = 'Professional' AND EducationLevel = 'Bachelors' GROUP BY FirstName ;



"""