carrinho = []

def add_item_cart(item):
    carrinho.append(item)
    return carrinho

def get_all_item_cart():
    return carrinho
    
def execute():
    id_user = input("Insira o id do usuário:")
    id_produto = input("Insira o id do produto:")
    price_product = float(input("Insira o preço do produto:"))
    quantity_product = int(input("Insira a quantidade de produto:"))
    item = [id_produto, id_user, price_product, quantity_product]
    carrinho = add_item_cart(item)
    print(carrinho)

execute()

