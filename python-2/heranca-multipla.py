class Mae:
    def __init__(self, nome, cor_cabelo):
        self.nome = nome
        self.cor_cabelo = cor_cabelo
        
class Pai:
    def __init__(self, nome, cor_olho):
        self.nome = nome 
        self.cor_olho = cor_olho

class Filho(Mae, Pai):
    def __init__(self, nome, cor_cabelo, cor_olho, sobrenome):
        self.sobrenome = sobrenome
        Mae.__init__(self, nome, cor_cabelo)
        Pai.__init__(self, nome, cor_olho)

filho = Filho('Matheus', 'Preto', 'Azul')
print(filho.cor_olho)
