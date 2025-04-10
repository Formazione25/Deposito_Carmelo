import numpy as np

arr = np.array([1,2,3,4,5])

#indexing
print(arr[0])

#slicing
print(arr[1:3])

#Boolean indexing
print(arr[arr>2])

arr_2= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr_2)
#slicing sulle righe
print(arr_2[1:3])
#slicing colonne
print(arr_2[:,1:3])
#slicing misto
print(arr_2[1:,1:3])

arr5 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Slicing di base
print(arr5[2:7])

# Slicing con passo
print(arr5[1:8:2])

# Omettere start e stop
print(arr5[:5])
print(arr5[5:])

# Utilizzare indici negativi
print(arr5[-5:])
print(arr5[:-5])

arr6 = np.array([10,20,30,40,50])

# Utilizzo di un array di indici
indices = np.array([1, 3])
print(arr6[indices])

# Utilizzo di una lista di indici
indices = [0, 2, 4]
print(arr6[indices])
