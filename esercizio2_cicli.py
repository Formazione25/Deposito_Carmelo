#uso while finchè non abbiamo 5 numeri nella lista
numeri_pari = []
while len(numeri_pari) < 5:
    numero = int(input("inserisci numero"))
    if numero % 2 == 0:
        numeri_pari.append(numero)
        print("il numero è pari")
    else:
        print("il numero non è pari")
#stampa i numeri inseriti
print("5 numeri pari inseriti",numeri_pari)

