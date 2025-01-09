import functools

herfler = ["H", "E", "L", "L", "O"]

#! lambda evezine def acar sozu ile yaradilan funksiyadan istifade ederek eyni neticenin elde edilmesi.
def menim_funksiyam(accumulator, element):
    return accumulator + element

soz = functools.reduce( menim_funksiyam, herfler)

print(soz)