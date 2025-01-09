# Environment variables 

# Muhit deyiskenlerinin deyerlerini ayri-ayri elde etmek ucun hemin deyerin acar sozunu 
# get() metodu ile elde etmek mumkundur.


import os

muhitDeyiskenleri = os.environ.get('__CFBundleIdentifier')

print(muhitDeyiskenleri)