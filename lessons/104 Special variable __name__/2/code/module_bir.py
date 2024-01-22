# 2 fayl yaradiriq. 

# 1cisinin adi:  module_bir
# 2cisinin adi:  module_iki - (ici bosdur)

# module_iki -ni import edirik ve asagida hemin fayl ucun xususi variable olan: __name__ variable-ini cagiririq.
# Netice olaraq elde etdiyimiz deyer: hemin faylin adi olacaqdir.
import module_iki


#? netice __main__ 
print (__name__)

#? netice module_iki 
print (module_iki.__name__)