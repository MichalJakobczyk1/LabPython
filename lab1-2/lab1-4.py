products = input("Podaj listę produktów po przecinku: ").replace(' ','')
print(products)
products_list = products.split(",")
print(products_list)
products_list_set = set(products_list)
print(products_list_set)
products_dict = {}

for product in products_list_set:
    print(product)
    products_dict[product] = float(input("Podaj wartosć produktu: "))
print(products_dict)