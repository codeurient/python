# Burda boyuk herf kicik herf ferqi vardir. yeni, "qayci" evezine "Qayci" yazsaq iki ferqli deyer kimi 
# qebul edilecekdir bu. 
import random

secmek = ["qayci", "kagiz", "qaya"]
komputer = random.choice(secmek)

# Biz boyuk herf ile yazsaq da bunu kicik qebul etmesi ucun lower() metodundan istifade edirik.
oyuncu = None
while oyuncu not in secmek:
    oyuncu = input("qayci, kagiz yoxsa qaya ?: ").lower()

print("Komputer: ", komputer)
print("Oyuncu: ", oyuncu)