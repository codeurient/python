import numpy as np

qutu1 = np.array(  [     [  [30, 40], [60, 20]  ]     ]  )
qutu2 = np.array(  [     [  [30, 20], [10, 20]  ]     ]  )


# - cixma operatoru array-in deyerlerini bir birinden cixartmaq ucun istifade edilir.
# ic-ice array-lar olsa bele say uygun geldiyi muddetce deyerler cixila da biler tolanada biler ve.s

print(  qutu1 - qutu2   )       # [  [     [0 20] [50 0]    ]  ]