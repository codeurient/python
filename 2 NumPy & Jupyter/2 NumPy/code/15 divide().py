import numpy as np

qutu1 = np.array(  [     [  [30, 40], [60, 20]  ]     ]  )
qutu2 = np.array(  [     [  [30, 20], [10, 20]  ]     ]  )


# divide() - bu metod bolme emeliyyati icra edir.

# Ana deyerler tam ededler olsa bele divide() metodu boldukden sonra kesir 
# ededler qaytaracaqdir. Tam edler elde etmek ucun astype() metodundan istifade etmek olar,
# yaxud boldukden sonra tam hisseni qaytarmasi ucun bu operatordan istifade etmek olar: // 

print(  qutu1 / qutu2             )       # [  [     [1.   2.] [6.   1.]    ]  ]
print(  np.divide(qutu1, qutu2)   )       # [  [     [1.   2.] [6.   1.]    ]  ]