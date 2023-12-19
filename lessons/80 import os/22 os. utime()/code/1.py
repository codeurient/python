# 1) ctime() - creation time: fayllar yaradilir

# 2) atime() - access time: yaradilan fayllar açılaraq içinə baxılır

# 3) mtime() - modification time: faylların içində hər-hansısa bir dəyişiklik edilir. 
# Yəni, ora nəsə əlavə etmək yaxud ordan nese silmek olar. Buna fayl icinde edilen deyisiklik deyilir

# Fayllar yaradilqida, açıldıqda, içində dəyişikliklər edildikdə avtomatik olaraq bir tarix yaranır.
# Faylin yaradilma tarixi, faylin açılma tarixi, faylin deyisdirilme tarixi.

# utime() - update time: bu metod ise fayllarin tarixlerini deyisdirmek ucun istifade edilir.
# Ancaq bu metod sadece faylin açılma (atime) ve faylda edilen deyisiklik (mtime) tarixini 
# deyisdire biler.

# utime() metodundan istifade ederek "atime" ve "mtime"-lari deyisdirdikde hemin fayllar ilk defe
# ne vaxt açılıb yaxud deyisdirilib oyrene bilmirik. Ancaq ilk yaranma (ctime) tarixi oldugu kimi qalir.