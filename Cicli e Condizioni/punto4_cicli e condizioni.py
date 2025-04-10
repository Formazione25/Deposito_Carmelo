#ciclo per aggiungere numeri alla lista
lista_numeri=[]
while len(lista_numeri) < 4:
    numero = int(input("inserisci numero"))
    lista_numeri.append(numero)
    print(lista_numeri)
print(lista_numeri)
#individuare il massimo della lista
max=max(lista_numeri)
max2= 0

for i in lista_numeri:
    if i> max2:
        max2=i

print("il numero massimo è",max2)

#conteggio dei numeri nella lista
conteggio=0
i=0

while i< len(lista_numeri):
    conteggio +=1
    i += 1

print("il conteggio è ",conteggio)

#verificare se lista è vuota e altrimenti stampare massimo e conteggio   
lista_vuota=[""]

if lista_numeri == lista_vuota:
    print("lista vuota")
else: 
    print("il conteggio è ",conteggio, "è il max è ",max2)

