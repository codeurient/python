"""

SELECT *, ROW_NUMBER() OVER(PARTITION BY product_details.Price) FROM amakon.product_details;



-- row_number() - bu funksiya qrup halina gelen deyerlere sıra nömrəsi teyin etmek ucun istifade edilir.
-- Her deyer usun bir sira nomresi teyin edir. Yalniz oxsar deyerler olduqda sira nomresi bele olur: 1,2,3,4,5 ve.savepoint


"""