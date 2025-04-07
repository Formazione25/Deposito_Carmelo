lista_dati = [1,2,3,4,5]
lista_dat2 = [1,"due",True,4.5]

print(lista_dat2[3])

lista_dati[0]=20

lista_dati.sort()
print(lista_dati)

inserimento = int(input("inserisci un numero"))
lista_dati.append(inserimento)

print(lista_dati)

#if else 
numero = 2
if numero > 0:
    print("Il numero è positivo")
    if numero == 100:
        print("woow")
elif numero == 2:
    print("ciao")
    

nome= input("inserisci nome")
if nome.lower == "ciao":
    print("woow")
