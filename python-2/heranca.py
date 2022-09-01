class Witch:
    def __init__(self, name, patron, house, color_eyes):
        self.name = name
        self.patron = patron
        self.house = house
        self.color_eyes = color_eyes
        
    def get_name(self):
        return f"O nome do(a) Bruxo(a) é: {self.name}"
    
    def getHouse(self):
        return f"Ele(a) está na casa {self.house}"
    
    def getPatron(self):
        return f"Seu patrono é {self.patron}"
    
class Harry(Witch):
    def __init__(self, name, patron, house, color_eyes, type_witch):
      self.type_witch = type_witch
      
      super().__init__(name, patron, house, color_eyes)
    
    def get_type_witch(self):
        if self.type_witch == 'P':
            return f"Este bruxo é sangue puro"
        
        if self.type_witch == 'M':
            return f"Este bruxo é Mestiço"
        
        return f"Este é um trouxa*"
    
harry = Harry('Harry Potter', 'Cervo', 'Sonserina', 'Verde/Azul?', 'M')
print(harry.get_type_witch())