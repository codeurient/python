# insert() - bu metoddan list -in icine deyer elave etmek ucun istifade edilir

# yeni list-in icinde istediyimiz yere istediyimiz deyeri elave ede bilerik

# 1ci arqumnet hara elave etmek isteyirik onu bildirir
# 2ci arqumnet ne elave etmek isteyirik onu bildirir

# Burda 2ci indekse "doner" deyerini elave edirik

yemek = ["pizza", "pendir", "dolma", "merci"]

yemek.insert(2, "doner")

for deyerler in yemek:
    print(deyerler)


