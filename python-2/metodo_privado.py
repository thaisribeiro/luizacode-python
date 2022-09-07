class RH:
    def __init__(self, funcao):
        self.funcao = funcao
        
    def __salario(self):
        return "Somente os adm podem ver"
    
    def holerite(self):
        return "Todo mundo pode ver"
        
    def ver_salario(self, responsavel):
        if responsavel == 'Taci' and self.funcao == 'ADM':
            return self.__salario()

        return 'Nao ve'
    
taci = RH('ADM')
print(taci.funcao)

fulano = RH('DEV')
salario_fulano = fulano.ver_salario('Taci')
print(salario_fulano)

salario_taci = taci.ver_salario('Taci')
print(salario_taci)