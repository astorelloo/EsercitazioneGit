somm= 0
while True:
    numero = int(input("Inserisci un numero intero (0 per terminare): "))
    if numero == 0:
        break
    somma += numero
print(f"La somma dei numeri inseriti è: {somma}")
