# 5 dene klas yaradiriq. XilasOlmaq, Yirtici, Dovsan, Sahin, Baliq
class XilasOlmaq:
    def qacmaq(self):
        print("Bu heyvan qacib xilas oldu")

class Yirtici:
    def ovlanmaq(self):
        print("Bu heyvan ovlanir")

# 'Dovsan' klasinin, 1 eded "XilasOlmaq" adinda ana klasi var
class Dovsan(XilasOlmaq):
    pass

# 'Sahin' klasinin, 1 eded "Yirtici" adinda ana klasi var
class Sahin(Yirtici):
    pass

# 'Baliq' klasinin, 2 eded "XilasOlmaq" ve "Yirtici" adinda ana klaslari var
class Baliq(XilasOlmaq, Yirtici):
    pass

dovsan = Dovsan()
sahin = Sahin()
baliq = Baliq()

# 'dovsan' klasinin obyekti sadece ana klasi olan "XilasOlmaq" klasinin metodunu gorur
dovsan.qacmaq()

# 'sahin' klasinin obyekti sadece ana klasi olan "Yirtici" klasinin metodunu gorur
sahin.ovlanmaq()

# 'baliq' klasinin obyekti ana klasi olan "XilasOlmaq" ve "Yirtici" klaslarinin metodlarini gorur
baliq.qacmaq()
baliq.ovlanmaq()


