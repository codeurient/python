# SELECT * FROM employeedb.employee2;

# # where ile sert qosaraq (in) employee1 de olan deyerler ile employee2 de 
# # olan deyerleri muqayise edirik ve ortax deyerleri olan setrleri elde edirik

# select FirstName, Department FROM employeedb.employee2
# where FirstName in (select FirstName FROM employeedb.employee1);
 