
#! 1) Standart kənarlaşma nədir? 
# Statistika , məlumatların təhlili, ehtimal nəzəriyyəsi və risklərin idarə edilməsində geniş istifadə edilən metodlardan biridir. 
# Gündəlik həyatda niyə geniş istifadə olunmur ? Bunun sebebi, standard kənarlaşmanın nisbətən çətin hesablanmasındadır. 
# Standart Kənarlaşmanı izah etmək üçün sadə bir misala baxaq: Şirkətdə 3 nəfər işçi çalışırsa, onların biri 
# 100 AZN, digəri 200 AZN , bir başqası 2000 AZN əmək  haqqı alır. Bu çoxluqun ədədi ortasına nəzər yetirdikdə 
# görürük ki, şirkət üzrə orta əmək haqqı 766 AZN-dir. Hazırda mühakiməni ona görə rahatlıqla yürütmək olduki, 
# qeyd olunan informasiyanın həcmi azdır. Rəqəmlər minlərlə olduqda isə artıq xüsusi funksiyalara ehtiyac qalır . 
# Standart kənarlaşma məhz bu funksiyalardan biridir. 

# Loru dilde desek. Verilen ededlerin ortasini tapiriq sonra ise bu tapdigimiz orta mexrece ne qeder uzaq ve ne qeder yaxin 
# oldugumuzu hesablayiriq. #! Standart kənarlaşma nece hesablanilir?
# a) Ortalama hesaplama:                    (x̄) = (0.8 + 0.78 + 0.91 + 0.77 + 0.54) / 5 = 0.776
# b) Hər bir elementin ortalamadan fərqi:   (0.8 - 0.776), (0.78 - 0.776), (0.91 - 0.776), (0.77 - 0.776), (0.54 - 0.776)
# c) Fərqlerin kvadratlarini tapiriq:       
        # (0.8 - 0.776)^2 = 0.0004, 
        # (0.78 - 0.776)^2 = 0.0004, 
        # (0.91 - 0.776)^2 = 0.01764, 
        # (0.77 - 0.776)^2 = 0.0004, 
        # (0.54 - 0.776)^2 = 0.05476
# d) Bu kvadratların cəmi:                  ∑(xi - x̄)^2 = 0.0004 + 0.0004 + 0.01764 + 0.0004 + 0.05476 = 0.0736
# e) Deyerlerin sayi:                       5   
# f) Dispersiyanin hesablanmasi:            σ^2 = 0.0736 / 5 = 0.01472
# g) Standart kənarlaşma:                   σ = √0.01472 ≈ 0.1214

# Eger standart kənarlaşma, ortalama deyere yaxin olsa idi, bu riskin az oldugu menasina gelecekdi.