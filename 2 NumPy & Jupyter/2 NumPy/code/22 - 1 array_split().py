
#? array_split() metodu array-i, alt array-lara bolmek ucun istifade edilir.
import numpy as np


qutu1 = np.array(  [  10, 20, 30, 40, 50, 60  ]  )
print(  np.array_split(qutu1, 3)   )   #! [  array([10, 20]),   array([30, 40]),   array([50, 60])  ]


# array_split metdu array elementlerinin uzunluqlarının fərqli olub-olmamasından asılı olmayaraq, 
# arraylari alt array-lara bölməyə icaze verir. 
qutu2 = np.array(  [  10, 20, 30, 40, 50  ]  )
print(  np.array_split(qutu2, 3)   )    #! [  array([10, 20]),   array([30, 40]),   array([50])  ]


# Yalniz, biz ozumuz array-i ferqli uzunluqda olan alt array-lara bolmek istedikde xeta alariq.
qutu3 = np.array(  [  [10, 20], [30, 40], [50]  ]  )                                #! ValueError: 
print(  qutu3  )


qutu4 = np.array(  [  np.array([10, 20]), np.array([30, 40]), np.array([50])  ]  )  #! ValueError: 
print(  qutu4  )
