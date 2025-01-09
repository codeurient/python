# copyfile() - bu metod movcud fayli kopyalamaq ucun istifade edilir.

# 1ci parametrde kompyalanan faylin adi yazilir.

# 2ci parametrde kopya kimi yaradilan faylin adi yazilir.

# Bu metodu cagirmaq ucun 'shutil' modulundan istifa edilir.

import shutil

shutil.copyfile('example.txt', 'copy.txt')