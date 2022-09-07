class Heroi:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def get_nome(self):
        return self.nome
    
    def skill(self):
        return "Não tem poder"
    
class HomemAranha(Heroi):
    def __init__(self, nome, idade, cidade):
        self.cidade = cidade
        super().__init__(nome, idade)

    def skill(self):
        return f"O poder do homem aranha é lançar teia"

class Flash(Heroi):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def skill(self):
        return "O poder de velocidade"

class Batman(Heroi):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
      
heroi1 = HomemAranha('Peter Park', '18 anos', 'NY')
heroi1.set_nome('Peter')
print('Poder Homem Aranha', heroi1.skill())

heroi2 = Flash('Barry Allen', '30 anos')
print('Poder do Flash', heroi2.skill())

heroi3 = Batman('Bruce', '50 anos')
print("Poder? Batman", heroi3.skill())
    
    
