import time

# localtime() funksiyasi ile elde edilen netice oxuna bilen formatda deyildir.
# Daha rahat bir format hazirlamaq ucun istifade edeceyimiz metodun adi beledir: #! strftime()  -  STRING FORMAT TIME
localVaxt =  time.localtime()  
print(localVaxt)

# strftime() metodu 2 parametr qebul edir. 
# 1ci parametr string kimi yazilan TELIMAT-lardir. #! TELIMAT-lari saytdan elde etmek olar: https://docs.python.org/3/library/time.html
# 2ci parametr localtime() funksiyasi ile elde etdiyimiz vaxtdir.
oxunaBilenFormat = time.strftime("%Y-%m-%d %H:%M:%S", localVaxt)
print(oxunaBilenFormat)