# LIKE xüsusi simvollar icinde yazilan şablonlardan istifadə edərək uyğun gelen deyerleri tapmaq üçün istifadə olunur.

#! Mesel ucun:
# 1) %      -   '%man'          Bu yazilis qaydasi "man" ilə bitən sətirlərə uyğun gəlir, buna görə də "foreman", "salesman" və s.kimi icinde "man" olan deyerler qayidacaq.
# 1) %      -   'mar%'          Bu yazilis qaydasi "man" ilə baslayan sətirlərə uyğun gəlir.
# 2 ) %     -   '%man%'         Bu o deməkdir ki, setrin istənilən yerində "man" alt sətiri olan sətirləri axtarırsınız.                            Meselen, "manager", "salesman" ve.s
# 3) _      -   't_st'          Bu icinde BIR simvol buraxilmis setrleri axtarmaq ucun istifade edilir.                                             Meselen, "test", "tast", ancaq "toast" yox.