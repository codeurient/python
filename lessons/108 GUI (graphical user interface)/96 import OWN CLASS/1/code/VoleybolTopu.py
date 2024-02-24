class VoleybolTopu:

    #! 1) 
    # Bu klasin avtomatik ozu ozunu cagiran __init__ adindaki metodundan istifade edirik. 
    # Bu metodun parametrleri yumru moterize icinde qeyd edilmisdir. 

    # 1ci parametr: self            - klasin ozudur. Cari senedin icinde klasin ozune muraciet etmek ucun istifade edilir.
    # 2ci parametr: canvas          - bu parametrin alacagi deyer '1.py' senedinin icinde 'VoleybolTopu()' klasi cagrildiqda verilir.
    # 3ci parametr: x               - bu parametrin alacagi deyer '1.py' senedinin icinde 'VoleybolTopu()' klasi cagrildiqda verilir.
    # 4ci parametr: y               - bu parametrin alacagi deyer '1.py' senedinin icinde 'VoleybolTopu()' klasi cagrildiqda verilir.
    # 5ci parametr: diametr         - bu parametrin alacagi deyer '1.py' senedinin icinde 'VoleybolTopu()' klasi cagrildiqda verilir.
    # 6ci parametr: xOxununSureti   - bu parametrin alacagi deyer '1.py' senedinin icinde 'VoleybolTopu()' klasi cagrildiqda verilir.
    # 7ci parametr: yOxununSureti   - bu parametrin alacagi deyer '1.py' senedinin icinde 'VoleybolTopu()' klasi cagrildiqda verilir.
    # 8ci parametr: reng            - bu parametrin alacagi deyer '1.py' senedinin icinde 'VoleybolTopu()' klasi cagrildiqda verilir.

    def __init__(self, canvas, x, y, diametr, xOxununSureti, yOxununSureti, reng):
        #! 2) 
        # self.canvasDeyiskeni  - bizim yaratdigimiz variable-dir.  canvas parametrinin aldigi deyeri, 'canvasDeyiskeni' variable-ina veririk. 
        # self.sekil            - bizim yaratdigimiz variable-dir.  canvas parametri Canvas() klasidir. Bu klasin create_oval() metodu ile daire yaradiriq ve 'sekil' variable-ina veririk.
        # self.xSureti          - bizim yaratdigimiz variable-dir.  xOxununSureti parametrinin aldigi deyeri, 'xSureti' variable-ina veririk. 
        # self.xySureti         - bizim yaratdigimiz variable-dir.  yOxununSureti parametrinin aldigi deyeri, 'xySureti' variable-ina veririk. 

        self.canvasDeyiskeni = canvas
        #! 3) 
        # Heleki burda istifade edilen variable budur.     
        # x         - 0-dir
        # y         - 0-dir
        # diametr   - 100-dur
        # fill      - "white"-dir
        self.sekil    = canvas.create_oval(x, y, diametr, diametr, fill=reng)  
        self.xSureti  = xOxununSureti
        self.xySureti = yOxununSureti
        