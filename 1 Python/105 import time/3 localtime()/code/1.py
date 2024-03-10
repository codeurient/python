import time

# localtime() funksiyasi, 9 elementli tuple() tipi qaytarir.
# Hansilardir bu 9 element ? 

#? 1. tm_year=2024
#? 2. tm_mon=1
#? 3. tm_mday=21
#? 4. tm_hour=9
#? 5. tm_min=27
#? 6. tm_sec=38
#? 7. tm_wday=6
#? 8. tm_yday=21
#? 9. tm_isdst=0

#! time.struct_time(tm_year=2024, tm_mon=1, tm_mday=22, tm_hour=10, tm_min=3, tm_sec=0, tm_wday=0, tm_yday=22, tm_isdst=0)


print(   time.localtime()   )