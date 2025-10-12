product_prices = {
    "alma" : 1.5,
    "portagal" : 2.0,
    "banan" : 1.8,
    "uzum" : 3.5,
}

budget = 2 # istifadecinin budjeti 10 manatdir

def check_budget(product, price, budget):
    
    if price <= budget:
        return f"{product} alinabilir. Qiytmet {price} manatdir."
    else: 
        return f"{product} alina bilmir. {price} manat, amma budcemiz yalniz {budget} manatdir."
    

while True:
    try:
        print("Movcud mehsullar: ")
        for product in product_prices:
            print(f" - {product}")
        
        selected_product = input("Hansi mehsulu almaq isteyirsiniz? (alma, portagal, banan, uzum): ").lower()

        if selected_product in product_prices:
            price = product_prices[selected_product]
            result = check_budget(selected_product,  price, budget)
            print(result)
            break
        else:
            print('Secdiyiniz mehsul movcud deyil, zhemet olmasa yeniden cehd edin.')

    except Exception as e:
        print(f"Xeta bas verdi: {e}. Zehmet olmasa duzgun cavab daxil edin" )