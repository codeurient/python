# format() - bu string metodudur ve melumatlarin mueyyen formata salindiqdan sonra ekrana yazdirilmasi ucun istifade edilir.

# format() metodu bezekli morterize ile birlikde istifade edilir. {}. 

# format() metodundan gonderilen melumatlar avtomatik olaraq {} bezekli moterizelerin icinde yazilir. 

heyvan = "inek"
cisim = "qeder"

cumle = "{} saman yoluna {} cixa bilmez. Cunki samanlari yiye-yiye geder."

print(    cumle.format(heyvan, cisim)    )

