# SELECT * FROM demo1.emp_data;


# Bu komandani yazaraq cedveli goruntulemek mumkundur
# Istersek terminalda bele bunu ede bilerik. Bunun ucun ilk once:

# 1. mysql -u root -p
# 2. parolu daxil et
# 3. use demo1                          - DB-e kecid et
# 4. SELECT * FROM demo1.emp_data;      - cedveli goruntule. 


# ULDUZ * bu simvol her sey menasina gelir. Eger cedvelden bir nece sutunu yaxud bir sutunu 
# secmek lazimdirsa bele yaza bilerik:

# 1.  SELECT EEID FROM demo1.emp_data;
# 2.  SELECT EEID, Department FROM demo1.emp_data;