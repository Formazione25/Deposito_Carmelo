import sqlite3 

#creiamo database
conn = sqlite3.connect('scuola.db')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS studenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')
#creo ciclo che permette di scegliere nomi o rimuovere
while True:
    cosa_fare= input("cosa vuoi fare? Digita aggiungo, rimuovi o basta")
    if cosa_fare == "aggiungo":
        nome_inserito = input("inserisci nome")
        cur.execute("INSERT INTO studenti (nome) VALUES (?)",(nome_inserito,))
        conn.commit()
        cur.execute("SELECT * FROM studenti")
        righe = cur.fetchall()
        for r in righe:
            print(r)
    elif cosa_fare == "rimuovi":
        nome_da_rimuovere= input("nome da rimuovere dalla tabella? ")
        cur.execute("DELETE FROM studenti WHERE nome = (?)",(nome_da_rimuovere,))
        conn.commit()
        righe = cur.fetchall()
        for r in righe:
            print(r)
    else:
        break





