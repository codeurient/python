# varsayilan parametr deyeri teyin edirik.

# Mesel ucun funksiyani yaradan zaman sadece parametri yazsaq ancaq cagiran zaman deyer yazmasaq
# Onda xeta mesaji elde ederik. Bunun olmamasi ucun funksiyani yaradan zaman varsayilan deyer olaraq
# bir seyler yazmaq lazimdir. 

# Indi ise funksiyani 1 defeden cox cagira ve ferqli deyerler vere bilerik yaxud hec bir deyer vermesek
# bele hec bir xeta olmayacaq. Cunki varsayilan bir deyeri var artiq hemin funksiyanin parametrinin.

def hardan(olke = "Azerbaycan"):
  print("Hardan gelirsiz?: " + olke)

hardan("İsveç")
hardan("Hindistan")
hardan()
hardan("Brazilya")