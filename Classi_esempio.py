class Automobile:               # dichiaro la classe
    numero_di_ruote = 4         # attributo di classe
    def __init__(self, marca, modello):         # metodo costruttore
        self.marca = marca              # attributo di istanza
        self.modello = modello          # attributo di istanza
    def stampa_info(self):              #metodo di istanza
        print("l'automobile è una" ,self.marca, self.modello)

oggetto1_Automobile= Automobile("aste","mod12")
print(oggetto1_Automobile.marca)
print(oggetto1_Automobile.modello)

Automobile.stampa_info(oggetto1_Automobile)

class Calcolatrice:
    @staticmethod       #metodo statico
    def somma(a,b):
        return a +b
    
risultato = Calcolatrice.somma(5,3)
print(risultato)

class Contatore:
    numero_istanze = 0 #attributo classe
    def __init__(self):
        Contatore.numero_istanze += 1
    @classmethod            #usa la classe e non oggetto
    def mostra_numero_istanze(cls):
        print("Sono state create ",cls.numero_istanze, "istanze")

#creazione istanze
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()