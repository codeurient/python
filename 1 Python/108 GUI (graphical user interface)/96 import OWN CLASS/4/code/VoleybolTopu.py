class VoleybolTopu:

    def __init__(self, canvas, x, y, diametr, xOxununSureti, yOxununSureti, reng):
        self.canvasDeyiskeni = canvas
        self.sekil    = canvas.create_oval(x, y, diametr, diametr, fill=reng)  
        self.xSureti  = xOxununSureti # 1
        self.ySureti  = yOxununSureti # 1

    def hereket(self):
        #! 1 
        # 'koordinatlar' variable-inin icinde ne var? coords() metodu ile 'self.sekil'-in koordinatlarini elde ederek hemin variable-a vermisik.
        # Bu deyerler 'x1, y1, x2, y2' deyerleridir. Hemin deyerleri ayri ayri elde ede bilerik. Bunun ucun 
        # [] kvadrat moterize ile muraciet etmeliyik. Sonra ise indekslerinin komekliyi ile hemin deyerleri cagira bilerik. 
        # 0-ci indeks - x1  - Bu, yumru dairenin yuxarı sol küncünün x koordinatıdır.
        # 1-ci indeks - y2  - Bu, yumru dairenin yuxarı sol küncünün y koordinatıdır.
        # 2-ci indeks - x2  - Bu, yumru dairenin aşağı sağ küncünün x koordinatıdır. 
        # 3-ci indeks - y2  - Bu, yumru dairenin aşağı sağ küncünün y koordinatıdır. 
        koordinatlar = self.canvasDeyiskeni.coords(self.sekil)
        #! 2 
        # Asagida yazdigimiz kod 506 qaytarmalidir. Ancaq 1ci novbede 506 evezine 1 yazdirilir ekrana. Niye ? Cunki, winfo_width() metodu ilk dəfə 
        # çağırılanda Tkinter hələ konfiqurasiya edilməmiş olur. Tkinter pəncərəsini (və onun bütün uşaq vidcetlərini) yaratarkən, onların standart 
        # ölçüləri 1 ola bilər, çünki vidjetlərin hələ işə salınma prosesindən keçməmis olma ehtimali vardir.
        # print(self.canvasDeyiskeni.winfo_width())

        # Burda koordinatlar[2] nin deyeri 100-dur.   self.canvasDeyiskeni.winfo_width()-in deyeri 1 olur. Yeni: 100 >= 1 olur ilk once (True)
        # Sonra ise, Tkinter tam konfiqurasiya edilir ve 1 evezine 506 deyerini elde edirik. Yeni: 100 >= 506. (False)

        # Bir sual daha: Canvas()-in olculerini 500px teyin etmisik, ancaq winfo_width() metodu Canvas()-in olculerini 506 olaraq bize qaytarir.
        # Niye? Cunki daxili bolsuq (padding) ve serheddin (border) olculeride cercivenin ustune elave edildikde 506px elde edirik. 
        # Eger bunun bas vermesini istemirsinizse, onda bele ede bilersiniz: #! Canvas(pencere, width=WIDTH, height=HEIGHT, bd=0, highlightthickness=0)
        print(self.canvasDeyiskeni.winfo_width())

        if(koordinatlar[2] >= self.canvasDeyiskeni.winfo_width() ):
            print(self.canvasDeyiskeni.winfo_width())

        self.canvasDeyiskeni.move(self.sekil, self.xSureti, self.ySureti) 