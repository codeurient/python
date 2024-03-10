# hist() - funksiyası verilənlər dəstindəki dəyərləri xüsusi diapazonlara bölür və hər diapazondakı dəyərlərin 
# tezliyini göstərən sütunlar yaradır. Beləliklə, məlumat dəstindəki dəyərlərin paylanmasını daha asan 
# başa düşə bilərik.


import matplotlib.pyplot as plt


x = [30, 40, 68, 27, 47, 59, 47, 88, 44, 23, 44, 66, 66, 35, 5, 100, 5, 50, 12, 17, 16, 100]

#! bins = 4 yəni verilenler dord-dord paylasdirilsin demekdir. Histoqram uzerinde çubuxların
#! neçə-neçə paylaşdırılması lazımdır demək üçün istifadə edilir.

plt.hist(x,  bins=4,   edgecolor='black',    color='pink')
# plt.hist(x,  bins=len(x),   edgecolor='black',    color='pink')
plt.show()