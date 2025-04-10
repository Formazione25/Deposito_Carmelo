import numpy as np
arr = np.linspace(0,1,12)
print(arr)

arr2= arr.reshape(3,4)
print(arr2)

random_arr = np.random.rand(3,4)
print(random_arr)

somma1= np.sum(arr2)
somma2= np.sum(random_arr)

print(somma1)
print(somma2)

#array
class ClasseArray: 
    def __init__(self, dati):
        self.arr = np.array(dati)
    def stampa(self):
        print("Array:", self.arr)

dati = [10, 20, 30, 40, 50]

arr_mio = ClasseArray(dati)
arr_mio.stampa()


#utilizzo funzione
def somma_arr(x):
    x = np.sum(x)
    return x

somma_funzione= somma_arr(arr)
print(somma_funzione)

#utilizzo somma con classe
class Calcola_somma:
    @staticmethod
    def somma_arr(x):
        x = np.sum(x)
        return x
    print(somma_funzione)

Calcola_somma.somma_arr(arr2)
somma_classe=Calcola_somma.somma_arr(arr)
print(somma_classe)