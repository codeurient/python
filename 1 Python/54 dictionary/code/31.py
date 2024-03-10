import json

telebe_melumatlari = {"ad": "Kamal", "yash": 16, "bal": 655}
# open() metodu ile fayli yaradiriq.
    # 1ci parametr yaradilan faylin adi.
    # 2ci parametr hemin faylin icine bir seyler yazmaq ucun yaradildigini bildirir.
fayl = open('demo.json', 'w')

# sort_keys - parametri, melumatlari elifba sirasina gore nizamlayir.
melumat = json.dumps(telebe_melumatlari, indent=4, sort_keys=True)

# write() metodu melumatlari demo.json faylinin icine yazir.
fayl.write(melumat)