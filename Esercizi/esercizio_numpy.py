#importo numpy
import numpy as np
#creo array e stampo
arr=np.arange(10,50)
print(arr)
print(arr.dtype)
#creo nuovo array con tipo dato "float64" e stampo forma
arr2=np.array(arr,dtype='float64')
print(arr2)
print(arr2.dtype)
print(arr2.shape)


