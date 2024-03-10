
#? Google hesaba daxil olaraq "2-step verification" ozelliyini aktivlesdirmek lazimdir. 
#? Ilk once 1) 'Manage your Google Account' bolmesine daxil olursuz
#? Sonra    2) "Security" bolmesine basaraq, asagida ki, "2-Step Verification" sozune basmaq lazimdir.
#? Sonra    3) "Get Started" duymesini basiriq.
#? Sonra    4) "Continue" duymesini basiriq.
#? Sonra    5) Telefon nomre Azerbaycan ucun desteklenmir deye "USE ANOTHER BACKUP OPTION" duymesini basiriq.
#? Sonra    6) Ilk once, 6 nomreli sekilde gorduyunuz kodlari "DOWNLOAD" edirsiz. Sonra ise "NEXT" duymesini basirsiz.
#? Sonra    7) "NEXT" dedikden sonra, 7 nomreli sekilde gorduyunuz "TURN ON" duymesini basiriq. Diger sehifeye kecid etdikde, sehifeni asagi surusdurun.
#? Sonra    8) Sehifeni en asagi saldiqdan sonra 8 nomreli sekilde isarelediyim "App password sozunu secirisz"
#? Sonra    9) "9.png" nomreli sekilde oldugu kimi giris teleb etse eger, yeniden parolu yazaraq hesaba daxil oluruq.
#? Sonra    10) "10.png" nomreli sekilde qirimiz ile isaretlediyim yerde ne istesez yaza bilersiz. Meselen men 'WEBSITE' yazdim. Sonra "Creat" duymesini basiriq. 
#? Sonra    11) "11.png" nomreli sekildeki google-un verdiyi parolu kopyalayirisiz ve Done sozune basaraq tamamlayirsiz işi.
#? Sonra    12) Bu parol her defe hamida ferqli olur, eyni olmur. Kopyalanan parolu "12.png" de yaratdigimiz 'parol' variable-ina yaziriq.
import smtplib

gonderen    = "davud.mehdiyev05@gmail.com"
qebuleden   = "codeurient@gmail.com"
parol       = "rjdi gvsu npwx bsxm"
movzununAdi = "Python ile email gonderme"
movzu       = "Men senin ucun bir mektub yazdim"

# Python-da, 3 dene cut dirnaq ne demekdir? Eger alt-alta 1-den cox setr yaratmaq isteyirikse, onda 3 dene cut dirnaq-dan istifade etmeliyik.
mesaj = f""" 
    Kimden: Davud Mehdiyev {gonderen}
    Kime: Afer Bayramov {qebuleden}
    Movzu: {movzununAdi}\n
    {movzu}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(gonderen, parol)
    print("Giris edildi...")
    server.sendmail(gonderen, qebuleden, mesaj)
    print("Mesaj gonderildi...")
except smtplib.SMTPAuthenticationError:
    print("daxil olmaq olmur")