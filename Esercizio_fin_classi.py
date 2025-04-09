#creo classe libro
class Libro():
    
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def stampa(self):
        print(self.titolo)
        print(self.autore) 
        print(self.pagine)
#classe Biblioteca
class Biblioteca():
    libri= []
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, titolo, autore, pagine):
        libro = Libro(titolo, autore, pagine)
        self.libri.append(libro)

    def stampa_libri(self):
        for x in self.libri:
            x.stampa()

Biblioteca_aggiornata= Biblioteca()
#ciclo per inserire libro
while True:
    titolo = input("inserisci il titolo")
    autore = input("inserisci l'autore")
    pagine = int(input("inserisci il numero pagine"))
    
    Biblioteca_aggiornata.aggiungi_libro(titolo,autore,pagine)
    
    Biblioteca_aggiornata.stampa_libri()

    scelta = input("Ripetere?")
    if scelta == "si":
        continue
    else:
        break
    
