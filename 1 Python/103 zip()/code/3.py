istifadeciAdi = ["Xalid", "Sahin", "Harun"]

parol = ("12345", "abc123", "qwerty5")

# qayidan deyerleri list(), tuple(), dict() kimi metodlar vasitesi ile istediyimiz kimi elde ede bilerik.
istifadeci = dict(   zip(istifadeciAdi, parol)   )

for acar, deyer in istifadeci.items():
    print(   acar + ": " + deyer   )