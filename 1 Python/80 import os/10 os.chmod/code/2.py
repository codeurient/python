# Kodu iwe saliriq ve yeniden bele bir xeta ile qarwilawiriq.

# /Library/Frameworks/Python.framework/Versions/3.11/Resources/Python.app/Contents/MacOS/Python: 
# can't open file '/Users/proj/domains/PYTHON/main.py': [Errno 13] Permission denied

# Bu o demekdir ki, Bizim nəinki faylı oxumaq ucun olan icazemiz, hətta həmin faylda Python 
# kodunu işə salmaq ucun olan icazəmiz de yoxdur.

# Hemin icazeni almaq ucun bu kodu yaziriq:
# chmod +x /Library/Frameworks/Python.framework/Versions/3.11/Resources/Python.app/Contents/MacOS/Python

import os, stat

try:
    os.chmod('/Users/proj/domains/PYTHON/test.txt', stat.S_IWRITE)
    print("Fayla muraciet etme huququ ugurla deyiwdirildi")

except OSError as e:
    print(f"Muraciet etme huququnu deyisme xetasi: {e}")
