# chdir - change directory sozunun qisaldilmasidir. Yəni, qovlugu deyismek.

# Bu metod emeliyyat sisteminde hal hazirda oldugumuz qovlugu bawqa qovluga deyiwmek ucun
# istifade edilir. 

import os

yol1 = os.getcwd()
print (yol1)

os.chdir( "numune" )

yol2 = os.getcwd()
print (yol2)