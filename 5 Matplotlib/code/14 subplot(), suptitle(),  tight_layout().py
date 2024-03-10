# subplot()      funksiyası çoxlu subqraflar yaratmaq üçün istifadə olunur. Bu funksiya diaqram daxilində çoxlu alt diaqram yaradır.
# suptitle()     funksiyası diaqramin esas başlığıni müəyyən etmək üçün istifadə olunur.
# tight_layout() funksiyası sub diaqramlar arasinda bosluq qoymaq üçün istifadə olunur.

import matplotlib.pyplot as plt

# 1ci arqument - row
# 2ci arqument - cols
# 3cu arqument - index

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Data1')

plt.subplot(2, 2, 2)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r--')  # Qirmizi kesikli xett
plt.title('Data2')


plt.subplot(2, 2, 3)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'go')  # Yasil daireler
plt.title('Data3')


plt.subplot(2, 2, 4)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bs')  # Mavi kvadratlar
plt.title('Data4')


plt.suptitle('Esas basliq')  
plt.tight_layout()  
plt.show()      