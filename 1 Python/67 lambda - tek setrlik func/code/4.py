# bu variable-a True veririk eger arqument ile gonderilen deyer
# gosterilenden boyuk olarsa eks halda False veririk

ededi_yoxla = lambda yas: True if yas >= 18 else False

print(  ededi_yoxla(15)  )