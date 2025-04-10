import numpy as np

#creazione array unidimensionale
arr = np.array([1,2,3,4,5])

#creazione array bidimensionale
arr2 = np.array([[1,2,3,], [4,5,6]])

print(arr)
print(arr2)

print("Forma:", arr2.shape)
print("Dimensioni dell'array:", arr.ndim)
print("Tipo di dati:", arr.dtype)
print("Numero di elementi:", arr.size)
print("Somma degli elementi:", arr.sum())
print("Media degli elementi:", arr.mean())
print("Valore massimo:", arr.max())
print("Indice del valore massimo:", arr.argmax())


#creato array con all'intero un range fino al numero 9
arr4= np.arange(10)
print(arr4)

#modifichiamo forma con reshape
arr5= np.arange(6)
print(arr5.shape)
print(arr5)
reshaped_arr5= arr5.reshape(3,2)
print(reshaped_arr5)