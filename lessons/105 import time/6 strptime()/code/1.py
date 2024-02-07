# strptime() - STRING PARSE TIME 

# Bu  metod 2 parametr qebul edir:
# 1ci parametr: STRING
# 2ci parametr: FORMAT

# CIXIS-da netice olaraq obyekt elde edirik.

import time

metnsel_vaxt = "20 April 2020"

vaxt = time.strptime(metnsel_vaxt, "%d %B %Y")

print(vaxt)