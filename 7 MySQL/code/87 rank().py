"""

SELECT *, rank() over(partition by product_details.Price order by product_details.Kids) FROM amakon.product_details;

-- rank() funksiyasi hər qrupdakı sətirləri, 'Kids' sütunundakı dəyərlərə görə siralayir.
-- Meselen: 0 - 1 kimi qebul edilir
-- Meselen: 1 - 2 kimi qebul edilir. Diger birlerde 2 kimi qebul edilir. 
-- Meselen: 1 - 2 kimi qebul edilir. 
-- Meselen: 1 - 2 kimi qebul edilir. 
-- Meselen: 1 - 2 kimi qebul edilir. 
-- Meselen: 1 - 2 kimi qebul edilir. 
-- Meselen: 1 - 2 kimi qebul edilir. Butun birlerin cemi 8 edir ve 1den sonra gelen 2 ededi 8 kimi qebul edilir.
-- Meselen: 2 - 8 kimi qebul edilir. 
-- Meselen: 2 - 8 kimi qebul edilir. 
-- Meselen: 2 - 8 kimi qebul edilir. 2 den sonra gelen 6 ededi 11 kimi qebul edilir. Yeni mentiq beledir:

-- 0 - 1 - 1
-- 1 - 2 - 2
-- 1 - 3 - 2
-- 1 - 4 - 2
-- 1 - 5 - 2
-- 1 - 6 - 2
-- 1 - 7 - 2
-- 2 - 8 - 8
-- 2 - 9 - 8
-- 2 - 10 - 8
-- 6 - 11 - 11

"""