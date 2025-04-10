import pandas as pd
import numpy as np

data = {
    "Prodotto": ['Prodotto2', 'Prodotto3', 'Prodotto2', 'Prodotto5', 'Prodotto6', 'Prodotto7'],
    'Quantità': np.linspace(20,60,6,dtype="int64"),
    'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma'],
    'Prezzo unitario': np.linspace(10,1000,6,dtype="int64")
    }

df = pd.DataFrame(data)
print(df)

# Aggiungiamo una nuova colonna
df['Totale Vendite'] = df['Quantità'] * df['Prezzo unitario']

print(df)

#raggruppare per prodotto
df_prodotto= df.groupby('Prodotto').agg({'Quantità': 'sum', 'Prezzo unitario': 'sum','Città':"first"})
print(df_prodotto)

#prodotto con più quantita
data_frame_prodotto= df.groupby('Prodotto')['Quantità'].sum().idxmax()

print(data_frame_prodotto)
