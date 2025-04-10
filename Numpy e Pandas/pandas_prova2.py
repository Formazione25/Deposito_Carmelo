import pandas as pd
import numpy as np
data = {
    "Nome": ['Alice', 'Bob', 'Carla'],
    'Età': [25, 30, 22],
    'Città': ['Roma', 'Milano', 'Napoli']
   }

df = pd.DataFrame(data)

# Stampa del DataFrame
print("DataFrame Originale: ")
print(df)

# Selezione righe età superiore a 23
df_older = df[df['Età'] > 23]

# Stampa righe
print("\nPersone con età superiore a 23 anni:")
print(df_older)

# Aggiungiamo una nuova colonna
df['Maggiorenne'] = df['Età'] >= 18

# Stampa nuovo DataFrame 
print("\nDataFrame con colonna 'Maggiorenne':")
print(df)

data2 = {
    "Nome": ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice', None],
    'Età': [25, 30, 22, 30, np.nan, 25, 29],
    'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma']
    }

df2 =pd.DataFrame(data2)
# Stampa del DataFrame
print("DataFrame Originale: ")
print(df2)

# Rimozione dei duplicati
df2 = df2.drop_duplicates()

# Rimozione delle righe dove almeno un elemento è mancante
df2_cleaned= df2.dropna()

# possiamo sostituire dati mancanti con valore di default
df2['Età'].fillna(df2['Età'].mean(), inplace=True)

# Stampa del DataFrame pulito
print("\nDataFrame dopo la pulizia:")
print(df2_cleaned)

# Stampa del DataFrame con dati mancanti sostituiti
print("\nDataFrame con dati mancanti sostituiti:")
print(df2)