import sqlite3 
conn = sqlite3.connect('miodatabase.db')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')

cur.execute("INSERT INTO utenti (nome) VALUES ('ciao')")
#salva modifiche
conn.commit()

#selezione 
cur.execute("SELECT * FROM utenti")

#mostare tutte le righe
righe = cur.fetchall()
for r in righe:
    print(r)


#funzione delete
cur.execute("DELETE FROM utenti WHERE id = 2")
conn.commit()
#mostra tutte le righe
righe = cur.fetchall()
for r in righe:
    print(r)

#sostituisco 
cur.execute("UPDATE utenti SET nome= 'name_new' WHERE id = 5")
conn.commit()

righe = cur.fetchall()
for r in righe:
    print(r)

conn.close()

