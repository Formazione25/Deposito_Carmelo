import pandas as pd
import numpy as np

Età_random = [np.linspace(20,60,6,dtype="int64")]
Salario_random = [np.linspace(0,1000,6,dtype="int64")]

print(Età_random)
print(Salario_random)

data = {
    "Nome": ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice'],
    'Età': [20, 28, 36, 44, 52, 60],
    'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma'],
    'Salario': [0,  200,  400,  600,  800, 1000]
    }

print(data)
df = pd.DataFrame(data)
print(df)

df_prime_5= df.head(5)
df_ultime_5= df.tail(5)

print(df_prime_5)
print(df_ultime_5)
print(df.dtypes)    

#calcolo media mediana e std
media_età =df['Età'].mean()
print(media_età)
mediana_età_età =df['Età'].median()
print(mediana_età_età)
std_età= df['Età'].std()
print(std_età)

#rimozione duplicati
df = df.drop_duplicates()
print(df)

# sostituzione
df['Età'].fillna(df['Età'].median(), inplace= True)



