# format() - bu string metodudur ve melumatlarin mueyyen formata salindiqdan sonra ekrana yazdirilmasi ucun istifade edilir.

# format() metodu bezekli morterize ile birlikde istifade edilir. {}. 

# format() metodundan gonderilen melumatlar avtomatik olaraq {} bezekli moterizelerin icinde yazilir. 

heyvan = "inek"
cisim = "ay"

cumle = "{} tullandi {} planetine qeder"

# 1ci parametr 1ci bezekli moterize 2ci parametr 2ci bezekli moterize icine avtomatik olaraq gonderilir. 
print(    cumle.format(heyvan, cisim)    )