# set kolleksiyasinin icinden en sonuncu elementi silmek ucun pop() metodundan istifade edilir

# Ancaq set -de siralama olmadigi ucun sonuncu elementin de ne oldugunu hec vaxt bilmirik

# Yeni sonuncu element istenilen element ola biler. Yeni silinen element istenilen element ola biler

# Asagidaki numunede "armud" silindi ancaq baxdiqda sonuncu olaraq "nar" elementini gorurduk
# Demeli proqrami ise saldiqda "armud" elementi kolleksiyanin sonuna kecmisdi ki, silindi

my_set = {"alma", "armud", "nar"}

my_set.pop()

print(my_set)