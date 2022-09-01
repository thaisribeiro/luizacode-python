
cart = []


def add_item_cart(item):
    cart.append(item)
    return 'success'


def get_all_items_cart():
    print('Carrinho =>', cart)
    return cart


def get_item_cart_by_id(id_product):
    for items_cart in cart:
        if items_cart[1] == id_product:
            print('Item =>', items_cart[1])
            return items_cart[1]


def remove_item_id(id_product):
    print('Antes da Remoção =>', cart)
    for items_cart in cart:
        if items_cart[1] == id_product:
            cart.remove(items_cart)

    print('Após Remoção =>', cart)
    return cart

item = []
i = 0
while i <= 2:
    id_user = input("Insira o id do usuário:")
    id_produto = input("Insira o id do produto:")
    price_product = float(input("Insira o preço do produto:"))
    quantity_product = int(input("Insira a quantidade de produto:"))
    item = [id_user, id_produto, price_product, quantity_product]
    add_item_cart(item)
    i += 1
    