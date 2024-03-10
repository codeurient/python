# Bu metod ici bos olan qovlugu silir

# Eger silmek istediyimiz qovlugun icinde her hansisa bir fayl yaxud qovluq olarsa onda xeta
# mesaji alariq. Cunki bu metod icinde fayl olan qovlugu silmir.

# Bunun ucun yeni icinde fayl olan qovlugu silmek ucun "shutil" modulunun 
# rmtree() metoundan istifade etmek lazimdir.

import os

yol = '/Users/proj/domains/PYTHON/numune'

os.rmdir(yol)