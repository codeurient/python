# Bu wekilde ferqli deyiskenlere deyerleri veribde yazmaq mumkundur.

import os

yol1 = 'Users'
yol2 = 'proj'
yol3 = 'domains'
yol4 = 'PYTHON'
yol5 = 'test.txt'


fayl_haqqinda = os.path.join(yol1, yol2, yol3, yol4, yol5)

print(  fayl_haqqinda  )