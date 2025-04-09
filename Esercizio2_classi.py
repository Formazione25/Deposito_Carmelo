#creare classe libro
class Libro():
    titolo=""
    autore=""
    pagine=0
    def __init__(self,titolo,autore,pagine):
        self.titolo= titolo
        self.autore= autore
        self.pagine= pagine
    def descrizione(self):
        return "Il Libro",self.titolo, "è scritto da",self.autore, "e ha pagine", self.pagine
        
#stampare descrizione
oggetto1_Libro= Libro("ciao","Cris",23)
print(oggetto1_Libro.descrizione())
