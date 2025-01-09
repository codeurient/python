# asagida qovluq1-in icindeki numune1.txt faylinin yerini deyiwerek qovluq2-nin icine gonderirik ve
# numune2.txt evez edilir numune1.txt fayli ile. 

# numune2.txt faylinin icindeki melumatlarda numune1.txt faylinin icindeki melumatlar ile 
# evez edilir. Yeni, numune2.txt faylinin butun melumatlari silinir evezinde numune1.txt'
# faylinin melumatlari gelir.

import os

yol1 = '/Users/proj/domains/PYTHON/qovluq1/numune1.txt'
yol2 = '/Users/proj/domains/PYTHON/qovluq2/numune2.txt'

os.replace(yol1, yol2)