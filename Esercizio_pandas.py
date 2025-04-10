import pandas as pd
import numpy as np

Età_random = [np.linspace(20,60,6,dtype="int64")]
Salario_random = [np.linspace(0,1000,6,dtype="int64")]

print(Età_random)
print(Salario_random)

data = {
    "Nome": ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice'],
    'Età': np.linspace(20,60,6,dtype="int64"),
    'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma'],
    'Salario': np.linspace(0,1000,6,dtype="int64")
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

#calcolo media mediana e std
media_salario =df['Salario'].mean()
print(media_salario)
mediana_salario =df['Salario'].median()
print(mediana_salario)
std_salario= df['Salario'].std()
print(std_salario)

#rimozione duplicati
df = df.drop_duplicates()
print(df)

# sostituzione
df['Età'].fillna(df['Età'].median(), inplace= True)

# Aggiungiamo una nuova colonna
df['Categoria_Età'] = np.where(df['Età'] < 18, 'Giovane',
                               np.where(df['Età'] <=95, 'Adulto', 'Senior'))

print(df)



