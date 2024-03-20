
#! SELECT * FROM classicmoels.payments;

# truncate() funksiyası verilmiş sütundakı kesir ədədi yuvarlaqlasdirmaq ucun istifade edilir.
# 1ci parametr yuvarlaqlasdirmaq istediyimiz ondaliq ededi nezerde tutur.
# 2ci parametr hemin ededin neçə vergul yuvarlaqlasmaq lazim oldugunu bildirir. 

# '112659.75'   -   0 olduqda   -   '112659'
# '112659.75'.  -   1 olduqda   -   '112659.7'
# '112659.75'.  -   2 olduqda   -   '112659.75'
# '112659.75'.  -   2 olduqda   -   '112659.75'
# ve.s. Ancaq 10 ve.s daha cox eded yazdiqda 2ci parametrde mesel ucun hemin 1ci parametrde olan ededin sonuna elave SIFIRLAR qoşmur.
# Yeni, bele etmir '112659.7500000000'
#! SELECT truncate(amount, 0) as `Amount` FROM classicmodels.payments	

# truncate() funksiyasini TRUNCATE kamandsasi ile sehf salmaq olmaz.	