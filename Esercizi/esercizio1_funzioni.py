#importo numero casuale
import random
#funzione indovina numero
def indovina_il_numero():
    numero_casuale = random.randint(1,100)
    while True:
        numero_inserito = input("Indovina numero (o digita 'esci'): ")
        if numero_inserito == 'esci':
            print("Uscito. Il numero era:", numero_casuale)
            break
        numero_inserito = int(numero_inserito)

        if numero_inserito == numero_casuale:
            print("Numero indovinato!")
            break
        elif numero_inserito < numero_casuale:
            print("Troppo basso!")
        else:
            print("Troppo alto!")
#eseguo funzione
indovina_il_numero()


