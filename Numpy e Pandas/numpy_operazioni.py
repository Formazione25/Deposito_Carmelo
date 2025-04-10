import numpy as np

#proviamo linspace
arr = np.linspace(0,1,5)
print(arr)

#proviamo random(matrice 3x3 con valori casuali)
random_arr = np.random.rand(3,3)
print(random_arr)

arr3= ([1,2,3,4,5])

sum_value= np.sum(arr3)
mean_value = np.mean(arr3)
std_value = np.std(arr3)

print("la somma è:", sum_value)
print("la media:", mean_value)
print("std:", std_value)