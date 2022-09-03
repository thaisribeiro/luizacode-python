cart = []

id_user = input("Insira o id do usuário:")
id_produto = input("Insira o id do produto:")
price_product = float(input("Insira o preço do produto:"))
quantity_product = int(input("Insira a quantidade de produto:"))

# id produto, id usuario, preço, quantidade
item = [id_produto, id_user, price_product, quantity_product]
def add_item_cart():
    cart.append(item)
    return cart

def get_all_items_cart():
    return cart
def get_item_cart_by_product(id_product):
    new_list = [item for item in cart if item[0] == id_product]
    return new_list[0]