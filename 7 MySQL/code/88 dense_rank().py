"""

SELECT *, dense_rank() 

over (partition by product_details.Product_name
order by product_details.kids)

FROM amakon.product_details;


-- rank() ile eyni isi gorur ancaq ondan ferqli olaraq eyni dəyərlər varsa, siralari oturmez.

"""