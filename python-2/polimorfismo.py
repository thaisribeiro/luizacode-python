class Boogeyman:
    def __init__(self):
        pass
    
    def form_boogeyman(self):
        return 'Indefinida'

class FearHarry(Boogeyman):
    def __init__(self, fear):
        self.fear = fear
        super().__init__()
        
    def form_boogeyman(self):
        return f"A forma do bicho-papão do Harry é: {self.fear}"

fear_harry = FearHarry("Dementador")
print(fear_harry.form_boogeyman())
    
    

      