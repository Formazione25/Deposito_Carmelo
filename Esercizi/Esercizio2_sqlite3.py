import sqlite3 

#senza classi
#creiamo database

""" cur.execute('''
    CREATE TABLE IF NOT EXISTS libri (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titolo TEXT,
        autore TEXT
    )
''')

#inseriamo titoli e autori
cur.executemany("INSERT INTO libri (titolo, autore) VALUES (?, ?)", [('Libro1', 'Autore1'), ('Libro2', 'Autore2'), ('Libro3', 'Autore3'), ('Libro4', 'Autore4')])
conn.commit()

#aggiungiamo colonna
cur.execute("ALTER TABLE libri ADD COLUMN Vendite TEXT")
conn.commit()

#valori casuali vendite
cur.execute("UPDATE libri SET Vendite = ABS(RANDOM() % 1000)")
conn.commit()

#stampiamo db
cur.execute("SELECT * FROM libri")
conn.commit()
righe = cur.fetchall()
for r in righe:
    print(r) """ 


#fatto con classi
#creiamo classe
class Libreria:
    def __init__(self, nome_db="libreria.db"):
        self.conn = sqlite3.connect(nome_db)
        self.cur = self.conn.cursor()
    def crea_tabella(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS libri (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titolo TEXT,
                autore TEXT
            )
        ''')
        self.conn.commit()
        print("Tabella 'libri' creata.")
    def inserimento_libri(self):
        self.cur.executemany("INSERT INTO libri (titolo, autore) VALUES (?, ?)", [('Libro1', 'Autore1'), ('Libro2', 'Autore2'), ('Libro3', 'Autore3'), ('Libro4', 'Autore4')])
        self.conn.commit()
    def aggiungi_colonna(self):
        self.cur.execute("ALTER TABLE libri ADD COLUMN Vendite TEXT")
        self.conn.commit()
    def valori_casuali(self):
        self.cur.execute("UPDATE libri SET Vendite = ABS(RANDOM() % 1000)")
        self.conn.commit()
    def stampa_tutto(self):
        self.cur.execute("SELECT * FROM libri")
        righe = self.cur.fetchall()
        if not righe:
            print("Nessun dato tabella.")
        else:
            print("Tabella 'libri':")
            for r in righe:
                print(r) 
    def chiudi(self):
        self.conn.close()
#creriamo istanza
libreria1 = Libreria()
#richiamo funzioni
libreria1.crea_tabella()
libreria1.inserimento_libri()
libreria1.aggiungi_colonna()
libreria1.valori_casuali()
libreria1.stampa_tutto()
libreria1.chiudi()
