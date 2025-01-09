# 3 klasimiz var. 
class Duzbucaqli:
    pass

# Kvadrat subclass-dir Ana klasi Duzbucaqli-dir
class Kvadrat(Duzbucaqli):
     def __init__(self, uzunluq, en):
        self.uzunluq = uzunluq
        self.en = en
    
# Kub subclass-dir Ana klasi Duzbucaqli-dir
class Kub(Duzbucaqli):
    def __init__(self, uzunluq, en, hundurluk):
        self.uzunluq = uzunluq
        self.en = en
        self.hundurluk = hundurluk

#//! Yuxarida her 2 subclass-da tekrarlanan kodlar hansilardir ?
# 1. self.en = en
# 2. self.uzunluq = uzunluq
# Kodun tekrarlanmamasi ucun nece ede bilerik ?
        
kvadrat = Kvadrat(3, 3)
kub = Kub(3, 3, 3)