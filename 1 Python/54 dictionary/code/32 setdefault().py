#!  setdefault(key, default_value) - açar sozden istifade ederek, lüğətin icinden dəyər əldə etmək üçün istifadə olunur. 
# Əgər açar artıq lüğətdə mövcuddursa, metod həmin açarın dəyərini qaytarır. Açar lüğətdə mövcud deyilsə, metod müəyyən edilmiş 
# açarı göstərilən dəyərlə birlikde daxil edir və həmin dəyəri qaytarır.



# setdefault() - açar sozun komekliyi ile, lüğət icinden dəyər əldə etmək üçün istifadə olunur.
# 1ci parametr acar sozdur. Eger hemin acar soz luget icinde movcuddursa, onda hemin acar sozun deyerini elde edirik.
luget1 = {'a': 1, 'b': 2, 'c': 3}
yeni_luget1 = luget1.setdefault('c')
print(    yeni_luget1   ) 



# 2ci parametr deyer teyin etmek ucun istifade edilir. Ancaq hemin acar sozun deyeri evvelceden movcud olarsa, onda
# setdefault() metodunun 2ci parametri hecne etmir.
luget2 = {'a': 1, 'b': 2, 'c': 3}
yeni_luget2 = luget2.setdefault('c', 5)
print(    yeni_luget2   )



# Eger bele bir acar soz ve deyer movcud deyildirse, onda setdefault() metodu, hem acar sozu yaradir hemde deyeri elave edir.
luget3 = {'a': 1, 'b': 2}
yeni_luget3 = luget3.setdefault('c', 5)
print(    luget3   )