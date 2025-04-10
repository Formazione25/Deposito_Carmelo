#funzioni
def saluta(nome):
    print("ciao")
    

#funzione con parametri
def somma (x,y):
    risultato= x+y
    print(risultato)

somma(1,2)

#funzione di ritorno
def riporta_dato(x):
    risultato = x*x
    return risultato

print(riporta_dato(3))

#funzione con parametri standard
def funzione_standard(x=1):
    return x+x
#sovrascrive x=1
print(riporta_dato(2))

