# path - bu kod os modulunun daxili moduludur. 

# Bu ders path daxili modulunun metodlarini inceliyesiyik

# os.path
# os.path.abspath(path)                 - ana qovlugun yolunu bize verir. 
# os.path.basename(path)                - qovluq adini iqnor edir ve faylin ozunun adini verir.
# os.path.commonprefix(list)            - fayllarin ortaq yerlewmiw oldugu ana qovlugun adini qaytarir.
# os.path.dirname(path)                 - faylin adini iqnor ediv ve sadece qovlugun adini verir
# os.path.exists(path)                  - faylin yaxud qovlugun var olub olmadigini yoxlayir
# os.path.expanduser(path)              - tilda ~ simvolunu istifadeci qovlugunun adi kimi qaytarir
# os.path.expandvars(path)              - environment (OS) variable-lara muraciet etmek ucundur
# os.path.getatime(path)                - fayla yaxud qovluga en son edilen muracietin tarixini qaytarir
# os.path.getmtime(path)                - sadece faylda edilen deyiwikliyin tarixini qaytarir
# os.path.getctime(path)                - sadece qovluqda edilen deyiwikliyin tarixini qaytarir
# os.path.getsize(path)                 - faylin olcusunu qaytarir. 
# os.path.isabs(path)                   - faylin yaxud qovlugun yolunun absolute olub olmadigini teyin edir.
# os.path.isfile(path)                  - yolun fayl olub olmadigini teyin edir.
# os.path.isdir(path)                   - yolun qovluq olub olmadigini teyin edir.
# os.path.islink(path)                  - yolun link olub olmadigini teyin edir.
# os.path.ismount(path)                 - bu metod mount nöqtəsinə qoşulmaq üçündür.
# os.path.join(path1[, path2[, ...]])   - emeliyyat sisteminden asili olaraq deyerleri yol formatina salir.
# os.path.normcase(path)                - fayllarin yaxud qovluqlarin yol adlarini duzgun formaya salir
# os.path.normpath(path)                - normaya uygun yazilmayan yollari duzelderek normal veziyyete getirir.
# os.path.realpath(path)                - faylin yerlesdiyi mutleq (absolute) yolu elde etmek ucundur.
# os.path.relpath((path, start=None)    - 2ci parametrdeki yola nisbeten 1ci parametrde olan yolun harda yerlewdiyini teyin edir.
# os.path.samefile(path1, path2)        - 
# os.path.sameopenfile(fp1, fp2)        -
# os.path.split(path)                   -
# os.path.splitdrive(path)              -
# os.path.splitext(path)                -
# os.path..supports_unicode_filenames   -