import numpy as np

qutu = np.array(  [     [10, 20, 30], [40, 50, 60], [70, 80, 90]     ]  )


# Eger sadece 1ci Array-in icindeki deyerlerin indexing-ini isteyirikse onda bele yaziriq.
print(  qutu[    0,    0:2   ]  )

# Eger sadece 2ci Array-in icindeki deyerlerin indexing-ini isteyirikse onda bele yaziriq.
print(  qutu[    1,    0:1   ]  )

# Eger sadece 3ci Array-in icindeki deyerlerin indexing-ini isteyirikse onda bele yaziriq.
print(  qutu[    2,    0:3   ]  )