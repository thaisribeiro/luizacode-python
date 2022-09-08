class Cart:
    def __init__(self):
        self.carts = []
    
    def add_item_cart(self, id_product, id_user, price_product, quantity_product):
        self.carts.append([id_product, id_user, price_product, quantity_product])    
        return self.carts

    def get_all_items_cart(self):
        return self.carts
    
    def get_item_cart_by_product(self, id_product):
        cart = [item for item in self.carts if item[0] == id_product]
        return cart[0]

    def remove_item_id_product(self, id_product):
        for i, el in enumerate(id_product):
            if el[0] == id_product:
                self.carts.remove(i)

    
        
cart = Cart()
