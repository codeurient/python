# 5 dene klas yaradiriq. Yalvarmaq, Yirtici, Dovsan, Sahin, Baliq
class Yalvarmaq:
    def qacmaq(self):
        print("Bu heyvan qacib xilas oldu")

class Yirtici:
    def ovlanmaq(self):
        print("Bu heyvan ovlanir")

# 'Dovsan' klasinin, 1 eded "Yalvarmaq" adinda ana klasi var
class Dovsan(Yalvarmaq):
    pass

# 'Sahin' klasinin, 1 eded "Yirtici" adinda ana klasi var
class Sahin(Yirtici):
    pass

# 'Baliq' klasinin, 2 eded "Yalvarmaq" ve "Yirtici" adinda ana klaslari var
class Baliq(Yalvarmaq, Yirtici):
    pass

dovsan = Dovsan()
sahin = Sahin()
baliq = Baliq()

# 'dovsan' klasinin obyekti sadece ana klasi olan "Yalvarmaq" klasinin metodunu gorur
dovsan.qacmaq()

# 'sahin' klasinin obyekti sadece ana klasi olan "Yirtici" klasinin metodunu gorur
sahin.ovlanmaq()

# 'baliq' klasinin obyekti ana klasi olan "Yalvarmaq" ve "Yirtici" klaslarinin metodlarini gorur
baliq.qacmaq()
baliq.ovlanmaq()


