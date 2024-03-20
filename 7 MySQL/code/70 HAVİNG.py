
#! SELECT * FROM demo1.emp_data;

# HAVING benzeyir WHEN komandasina ancaq WHEN komandasini GROUP BY ile istifade etmek mumkun olmadigi
# ucun WHEN evezine HAVING komandasindan istifade edirik.

# Burda Department adlarini EEID identifikatorlara gore secirik. Yeni neçə dənə EEID sayi aiddir IT departemintine ve.s
# Bunun ucun ilk once IT, Finance ve.s department adlarini qruplasdiririq. Yeni bir araya yigiriq. 
# Hemin department-ler bir araya yigildiqdan sonra count() ile neçə dənə EEID sayi aiddir IT departemintine ve.s deyirik.

# HAVING ile şərt qoşuruq ki, sayi 100-den cox olanlari elde edek.
#! select Department, count(EEID) from demo1.emp_data group by Department having count(EEID) > 150;