# Emeliyyat sisteminde environment variables deyilen bir termin var.

# environment variables nedir ? Mühit dəyişkənləri. 

# Bu deyiskenler emeliyyat sistemi terefinden evvelceden teyin edilmiwdir ve deyerler 
# verilmiwdir her deyiskene. 

# Hemin emeliyyat sisteminin deyiskenlerini ve deyerlerini elde etmek ucun ise 
# environ atributundan istifade edilir.

import os

muhitDeyiskenleri = os.environ

# items() metodundan muhit deyiskenlerini, Acar ve Deyer olaraq elde etmek ucun istifade edirik.

# Elde edilen Acarlar for dongusunde olan key deyiskenine verilir.
# Elde edilen Deyerler for dongusunde olan value deyiskenine verilir.
for key, value in muhitDeyiskenleri.items():
    print(f'{key}: {value}')
