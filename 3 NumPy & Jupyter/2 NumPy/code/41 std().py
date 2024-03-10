# std() metodu, array deyerlerinin bir-birine ne qeder yaxın yaxud ne qeder uzaq olduğunun ferqini qaytarır.
import numpy as np
qutu1 = [200, 300, 150, 130, 200, 280, 170, 188]
print(  np.std(qutu1)  )                    

#! 1) Вычисление среднего значения:
# 200 + 300 + 150 + 130 + 200 + 280 + 170 + 188 = 1618  / 8 = 202.25

#! 2) Разность между каждым элементом и средним значением:
# 200−202.25 = −2.25
# 300−202.25 = 97.75
# 150−202.25 = −52.25
# 130−202.25 = −72.25
# 200−202.25 = −2.25
# 280−202.25 = 77.75
# 170−202.25 = −32.25
# 188−202.25 = −14.25

#! 3) Квадраты отклонений:
# −2.25   ^2   =  5.0625
# 97.75   ^2   =  9555.0625
# −52.25  ^2   =  2730.5625
# −72.25  ^2   =  5220.0625
# −2.25   ^2   =  5.0625    
# 77.75   ^2   =  6050.5625
# −32.25  ^2   =  1039.5625
# −14.25  ^2   =  203.0625

#! 4) Вычисление среднего значения квадратов отклонений
 # 5.0625 + 9555.0625 + 2730.5625 + 5220.0625 + 5.0625 + 6050.5625 + 1039.5625 + 203.0625 = 24709.9375 / 8 = 3088.7421875

#! 5) Корень из среднего значения квадратов отклонений
#  3088.7421875 ededinin kokalti = 55.68157235567257

# Təsəvvür edək ki, sinifdəki şagirdlərin boyu haqqında məlumatımız var. Bu artımın ortalaması bizə orta hesabla hansı artımı gözləyə biləcəyimiz
# barədə ümumi fikir verəcəkdir. Bəs tələbələrin boyu fərqli olarsa necə? Bəziləri ortadan yuxarı, bəziləri isə aşağı ola bilər. Standart ferq bu 
# fərqlərin ortadan nə qədər böyük olduğunu anlamağa imkan verir. Əgər standart ferq böyükdürsə, bu o deməkdir ki, şagirdlərin boyu orta göstəricidən 
# kifayət qədər fərqlənir, kiçikdirsə, onların boyu daha çox oxşardır. Beləliklə, standart ferq bizə deyerlerin nə qədər "müxtəlif" və ya "oxşar" ola 
# biləcəyini anlamağa kömək edir.