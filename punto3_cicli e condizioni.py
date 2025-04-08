#ciclo che aggiunge numeri nella lista e poi stampa il quadrato di quei numeri
lista_numeri=[]
while len(lista_numeri) < 4:
    numero = int(input("inserisci numero"))
    lista_numeri.append(numero)
print(lista_numeri)

for i in lista_numeri:
    print(i**2)
