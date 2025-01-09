# write() - bu metod movcud faylin icine bir seyler yazdirmaq ucun istifade edilir.

# Eger fayl movcud deyilse bu metod hemin fayli yaradir ve yaratdiqdan sonra icine 
# bizim istediyimiz mezmunu yazdirir.

# open() metodu icinde 2ci parametr olaraq acdigimiz faylin oxunmaq (r) ucunmu 
# yazmaq (w) ucunmu oldugunu qeyd ede bilirik.

metn = "lorem ipsum dolor \n sit amet, sed \n diam nonum"

with open('example.txt', "w") as sened:
    sened.write(metn)