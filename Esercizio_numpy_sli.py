import numpy as np
#creo array
arr = np.random.randint(10,50,20)
print(arr)
#primi 10 elementi
print(arr[0:10])
#ultimi 5
print(arr[15:])
#dalla 5 alla 15
print(arr[5:15])
#ogni terzo elemento
print(arr[0:21:+3])
#modifica valori
arr[5:10]=99
print(arr)





