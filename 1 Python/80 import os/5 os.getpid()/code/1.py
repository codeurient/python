# Proqram kodunu her iwe saldiqda yeni bir unikal identifikator (ID) yaranir.

# Buna, icra edilen emeliyyat identifikatoru yaxud qisaca proses identifikatoru deyilir.

# Yeni, PID. Bu PID-i elde etmek ucun iste getpid() metodundan istifade edilir.


import os

melumat = os.getpid()

print(melumat)