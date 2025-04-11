import sqlite3 


conn = sqlite3.connect('scuola.db')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS studenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')
while True:
    nome_inserito = input("inserisci nome")
    cur.execute("INSERT INTO studenti (nome) VALUES (?)",(nome_inserito,))
    conn.commit()
    cur.execute("SELECT * FROM studenti")
    righe = cur.fetchall()
    for r in righe:
        print(r)
   