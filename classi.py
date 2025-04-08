#creazione classe
class Esempio():
    x=10

#creazione oggetto
oggetto_1 = Esempio()
oggetto_1.x = 20
print(oggetto_1.x)


class Penna():
    altezza = 0
    larghezza = 0
    #costruttore
    def __init__(self,h,l):
        self.altezza = h
        self.larghezza = l

oggetto_penna = Penna(10,7)

print(oggetto_penna.altezza)
print(oggetto_penna.larghezza)

oggetto_2_penna = Penna(5,6)
print(oggetto_2_penna.altezza)
print(oggetto_2_penna.larghezza)