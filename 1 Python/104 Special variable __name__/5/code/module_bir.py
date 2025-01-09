# Mesel ucun: numune() adinda funksiya yaradiriq. Bu funksiya if konstruksiyasinin icinde deyil.
# "module_bir.py" faylini iwe saldiqda burda olan butun kodlar (hem" numune()" hem if konstruksiyasi 
# icinde olan kodlar) iwleyecekdir. 

#! Ancaq "module_bir.py" faylini, import etsek "module_iki.py" faylinin icine, onda sadece "numune()"
#! adli funksiya iwleyecekdir. if konstruksiyasi icinde olan kodlar iwlemeyecekdir.

def numune():
    print("Salam necesen?")

def numune2():
    print("Kodlari ezberleyin")
numune2()


if __name__ == '__main__':
    numune()

else:
    print("bu modul dolayi yol ile işə salinmisdir")