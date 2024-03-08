import pandas as pd

data1 = {
    "Emp Id" : [ "E01", "E02", "E03", "E04", "E05", "E06"],
    "Names"  : [ "Jorc", "Bob", "Marry", "John", "David", "Mark"],
    "Age"    : [ 34, 56, 23, 44, 32 ,36]
}

data2 = {
    "Emp Id" : [ "E01", "E02", "E03", "E04", "E05", "E07"],
    "Salary"  : [ 45000, 56000, 34000, 30000, 50000, 62000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(pd.merge(df1, df2))
print('************************************************************')
# parametr yerlerinde hansi DataFrame() hansina birlesdirilsin, hansi sutun esas goturulsun, ferqli deyer varsa nezere alinsinmi alinmasin mi demek olur:
# left=df2, right=df1       - df2 birlesdirilsin df1 cedveline demis oluruq
# left=df1, right=df2       - df1 birlesdirilsin df2 cedveline demis oluruq
# on="Emp Id"               - hansi sutune esaslanaraq birlesdirilsin deyirik
# how='left'                - hansi cedvelin setrleri qorunsun demek ucun istifade edilir. left dedikde sol DataFrame setrleri qorunur
# how='right'               - hansi cedvelin setrleri qorunsun demek ucun istifade edilir. rihgt dedikde sag DataFrame setrleri qorunur
print(   pd.merge(left=df1, right=df2, on="Emp Id", how='right')   )