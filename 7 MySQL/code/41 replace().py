# SELECT * FROM demo1.emp_data;

# replace() metodu bir deyeri digeri ile evez etmek ucun istifade edilir.

# 1ci parametr - deyisiklik edilecek deyer, Yeni deyisiklik hansi deyer uzerinde aparilacaq hemin deyeri qeyd edirik.
# 2ci parametr - neyi evez edeceyik ?
# 3ci parametr - ne ile evez edeceyik ?
# SELECT LENGTH(REPLACE(REPLACE(`Annual Salary`, '$', ''), ',', '')) AS digitCount FROM demo1.emp_data;


# -- Indi ise elde edirik: 7 ve 6.  