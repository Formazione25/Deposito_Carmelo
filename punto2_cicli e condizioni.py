#ciclo che stampa lista numeri decrementando di uno
ripetere = "si"
while ripetere == "si":
        x = int(input("inserisci numero"))
        for i in range(x,-1,-1):
            print(i)
        ripetere= input("vuoi ripetere?").lower()
        if ripetere == "no":
            print("ok")
            break