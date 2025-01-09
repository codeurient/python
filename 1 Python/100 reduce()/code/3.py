# reduce() metodundan istifade ederek faktorial-in hesablanmasi.

import functools

faktorial = [1, 2, 3, 4, 5]

netice = functools.reduce(lambda x, y: x * y, faktorial)
print(netice)