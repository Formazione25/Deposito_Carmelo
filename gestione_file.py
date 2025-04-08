#lettura file
file = open("esempio_testo.txt","r")
tutte_le_righe = file.read()
riga = file.readline()

print(riga)

file.close()

#scrittura su file
file = open("esempio_testo2.txt","w")

file.write("ciaoooooo")
file.close()

#aprire con with
with open("esempio.testo3.txt","a") as file:
    file.write("ecco")
    