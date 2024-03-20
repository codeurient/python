
#! SELECT * FROM sakila.payment;

# datediff() funksiyası iki tarix arasındakı gun fərqini tapmaq üçün istifadə olunur

#! select datediff(last_update, payment_date) as Dates from sakila.payment;


# 2006-02-15 22:12:30 - 2005-05-25 11:30:37 = 266 gun