# mod-lar 2ci parametr olaraq yazilir. Hemin modlar bunlardir. Bu modlari yazmaq ucun 'stat' modulundan
# yaxud hemin modun qarwiligi olan sekkizlik (8 - octal) say sistemindeki qarwiligindan istifade etmek olar.

# os.chmod('/Users/proj/domains/PYTHON/test.txt', 0o200)

# stat.S_ISUID (Set user ID on execution)           - 0o4000
# stat.S_ISGID (Set group ID on execution)          - 0o2000
# stat.S_ENFMT (Record locking enforced)            - 0o2000
# stat.S_ISVTX (Save text image after execution)    - 0o1000
# stat.S_IREAD (Read by owner)                      - 0o400
# stat.S_IWRITE (Write by owner)                    - 0o200
# stat.S_IEXEC (Execute by owner)                   - 0o100
# stat.S_IRWXU (Read, write, and execute by owner)  - 0o700
# stat.S_IRUSR (Read by owner)                      - 0o400
# stat.S_IWUSR (Write by owner)                     - 0o200
# stat.S_IXUSR (Execute by owner)                   - 0o100
# stat.S_IRWXG (Read, write, and execute by group)  - 0o70
# stat.S_IRGRP (Read by group)                      - 0o40
# stat.S_IWGRP (Write by group)                     - 0o20
# stat.S_IXGRP (Execute by group)                   - 0o10
# stat.S_IRWXO (Read, write, and execute by others) - 0o7
# stat.S_IROTH (Read by others)                     - 0o4
# stat.S_IWOTH (Write by others)                    - 0o2
# stat.S_IXOTH (Execute by others)                  - 0o1

import os, stat

try:
    os.chmod('/Users/proj/domains/PYTHON/test.txt', stat.S_IWRITE)
    print("Fayla muraciet etme huququ ugurla deyiwdirildi")
except OSError as e:
    print(f"Muraciet etme huququnu deyisme xetasi: {e}")
