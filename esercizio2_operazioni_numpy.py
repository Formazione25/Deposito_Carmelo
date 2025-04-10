import numpy as np
#creo classe che gestisce 
class ClasseArray: 
    def __init__(self):
        self.linspace_arr = np.linspace(0, 10, 50)
        self.random_arr = np.random.random(50)
        self.nuovo = self.linspace_arr + self.random_arr
    def linspace(self):
        self.linspace_arr = np.linspace(0, 10, 50)
    def random(self):
        self.random_arr = np.random.random(50)
    def sommarr(self):
        self.nuovo = self.linspace_arr + self.random_arr
    def somma_totale(self): 
        return np.sum(self.nuovo)
    def somma_maggiori_5(self):
        return np.sum(self.nuovo[self.nuovo > 5])

    def stampa_tutto(self):
        print(self.linspace_arr)
        print(self.random_arr)
        print(self.nuovo)
        print(self.somma_totale())
        print(self.somma_maggiori_5())
#oggetto
ogg = ClasseArray()        
#richiamo
ogg.stampa_tutto()



    
    
