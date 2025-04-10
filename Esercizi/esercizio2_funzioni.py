#definire funzione
def fibonacci_n():
    numero = int(input("inserisci un numero: "))
    x= 0
    y=1

    while x <= numero:
        print(x)
        temp= x
        x = y
        y = temp + y
        
       
#eseguo funzione
fibonacci_n()