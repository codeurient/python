# load_dataset() funksiyasi, data-lari daxili Seaborn resurslarından yükləyir və onu DataFrame kimi təqdim edir.  
# barplot() funksiyasi, bar diaqramları yaratmaq üçün istifadə olunur.
    
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import seaborn as sns
import matplotlib.pyplot as plt


# Bu data hardan gelir bize ? Bu github linkinden avtomatik olaraq: https://github.com/mwaskom/seaborn-data
data = sns.load_dataset("tips")
print(data) 

sns.barplot(data=data,    x='day',     y='tip',     hue='sex',     order=['Sun', 'Sat', 'Fri', 'Thur'],    errorbar=('ci', 0))
plt.show()



#! SSL: CERTIFICATE_VERIFY_FAILED
# Eger bele bir xeta alsaniz. Bu xəta adətən Python, İnternetdən məlumat endirərkən SSL sertifikatını yoxlaya bilmədikdə baş verir. 
# Bezen bu xeta bir neçə səbəbə görə baş verə bilər, lakin çox vaxt səhv SSL konfiqurasiyası və ya şəbəkə məhdudiyyətləri ilə bağlıdır.

# 1 ci qayda: https evezine http istifade etmek 
# 2 ci qayda: SSL sertifikatının yoxlanılmasını deaktiv etmek:
    #? import ssl
    #? ssl._create_default_https_context = ssl._create_unverified_context