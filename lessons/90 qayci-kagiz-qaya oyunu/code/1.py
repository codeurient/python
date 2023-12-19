# 'random' modulunu import edirik sonra ise 'secmek' adinda bir list yaradiriq. 

# random modulunun choice() metodu ile list icinden ferqli deyerleri ekrana yazdira bilerik.

import random

secmek = ["qayci", "kagiz", "qaya"]

komputer = random.choice(secmek)

print(komputer)