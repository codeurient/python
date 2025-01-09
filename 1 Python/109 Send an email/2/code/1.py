import smtplib

gonderen    = "davud.mehdiyev05@gmail.com"
qebuleden   = "codeurient@gmail.com"
parol       = "rjdi gvsu npwx bsxm"
movzununAdi = "Python ile email gonderme"
movzu       = "Men senin ucun bir mektub yazdim"

mesaj = f""" 
    Kimden: Davud Mehdiyev {gonderen}
    Kime: Afer Bayramov {qebuleden}
    Movzu: {movzununAdi}\n
    {movzu}
"""
# SMTP() obyekti, poçt serveri ilə əlaqə yaradir. 
# a) 1ci parametrde hansi poct serveridirse onun adini yaziriq
# b) 2ci parametrde Port 587 şifrələnmiş poçtlar göndərmək üçün istifadə olunur
server = smtplib.SMTP("smtp.gmail.com", 587)
# starttls() - (Transport Layer Security - Göndərmə derecesinin tehlukesizliyi) - Bu metod, təhlükəsiz rabitə kanalı yaradaraq, poçtun 
# gonderilmesini temin edir.
server.starttls()

try:
    # login() metodu ile hesaba daxil oluruq.
    server.login(gonderen, parol)
    print("Giris edildi...")
    # sendmail() metodu ile neyin, kimden, kime gonderileceyini demek ucun istifade edirik.
    # a) 1ci parametr mesajin kim terefinden gonderileceyini teyin edir.
    # b) 2ci parametr mesajin kim terefinden qebul edileceyini teyin edir.
    # c) 3cu parametr hansi mesajin gonderileceyini teyin edir.
    server.sendmail(gonderen, qebuleden, mesaj)
    print("Mesaj gonderildi...")
# Eger xeta bas vererse hemin xetani gormek ucun try-except konstruktorundan faydalaniriq.
except smtplib.SMTPAuthenticationError:
    print("daxil olmaq olmur")