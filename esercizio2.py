lista = ["a","b","c","d"]

scelta = input("aggiungere rimuovere o modificare?")


if scelta == "aggiungere":
    aggiunta= input("cosa aggiungere? ")
    lista.append(aggiunta)
    print(lista)
elif scelta == "rimuovere":
    rimozione= input("cosa rimuovere? ")
    lista.remove(rimozione)
    print(lista)
elif scelta == "modifica":
    modifica= int(input("quale posizione?"))
    sostituzione=(input("con cosa sostituire? "))
    lista[modifica]= sostituzione
    print(lista)
else:
    print("comando errato")

        




