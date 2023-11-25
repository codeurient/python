# tuple tipinin deyerlerini deyismek mumkun deyildir.


def hesabla(*parametr): 
    cem = 0
    # Burda indeksi sifir olan yeni 4 ededine muraciet edirik ve onu 8 ededi ile evez etmeye calisiriq.
    # Ancaq parametr deyiskenin tipi tuple oldugu ucun, onu deyise bilmirik ve xeta aliriq
    parametr[0] = 8 
    for eldeEdilenDeyerler in parametr:
        cem += eldeEdilenDeyerler   
    return cem

print(  hesabla(4,6,2,4,3,8,5,4)  )