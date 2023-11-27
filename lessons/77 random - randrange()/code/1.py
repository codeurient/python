# randrange(start, stop, step) funksiyası təyin edilmiş aralıqda təyin edilmiş addımla 
# təsadüfi bir rəqəm qaytarır.

import random
# 0 ile 10 arasinda random bir eded qaytar. 2 ise addim sayini bildirir. Meselen:
random_eded1 = random.randrange(0, 10, 9) #  0 vere biler 9 eded addiyir ve 9                           vere biler  
random_eded2 = random.randrange(0, 10, 8) #  0 vere biler 8 eded addiyir ve 8                           vere biler   
random_eded3 = random.randrange(0, 10, 7) #  0 vere biler 7 eded addiyir ve 7                           vere biler  
random_eded4 = random.randrange(0, 10, 6) #  0 vere biler 6 eded addiyir ve 6                           vere biler  
random_eded5 = random.randrange(0, 10, 5) #  0 vere biler 5 eded addiyir ve 5                           vere biler  
random_eded6 = random.randrange(0, 10, 4) #  0 vere biler 4 eded addiyir ve 4, 8                        vere biler  
random_eded7 = random.randrange(0, 10, 3) #  0 vere biler 3 eded addiyir ve 3, 6, 9                     vere biler  
random_eded8 = random.randrange(0, 10, 2) #  0 vere biler 2 eded addiyir ve 2, 4, 6, 8                  vere biler  
random_eded9 = random.randrange(0, 10, 1) #  0 vere biler 1 eded addiyir ve 1, 2, 3, 4, 5, 6, 7, 8, 9   vere biler  

print(random_eded9)