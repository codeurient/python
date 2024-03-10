# fiter() - bu funksiya 2 parametr qebul edir: filter(function, iterable)
# 1ci parametri funksiyadir.
# 2ci parametri ise iterabe - yeni tekrarlana bilen obyektler.


#! filter() - bu metodun 1ci parametrinde bir funksiya olur. Hemin funksiya meselen if ile
# bir şərt qosur ve eger 2ci parametrden elde olunan deyerler hemin şərtə uyğun olarsa kod 
# mueyyen edilmis emeliyyati icra edir. 


ededler = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ededler list-inden alinan deyerler x deyiskenine verilir sonra 2 ededine bolunur.
# Eger qaliq sifira beraber olarsa True qayidar. Hemin True qayidan ededleri "cut_ededler"
# variable-ina gonderirik. 
cut_ededler = filter(lambda x: x % 2 == 0, ededler)

print(list(cut_ededler))