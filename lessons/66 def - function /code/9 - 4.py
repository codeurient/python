# tuple tipini list-e cevirerek evvelceden teyin edilmis deyeri ferqli bir deyere cevire bilerik.


def hesabla(*parametr): 
    cem = 0
    parametr = list(parametr)
    parametr[0] = 8 
    for eldeEdilenDeyerler in parametr:
        cem += eldeEdilenDeyerler   # 8 + 6 + 2 + 4 + 3 + 8 + 5 + 4 = 40
    return cem

print(  hesabla(4,6,2,4,3,8,5,4)  )