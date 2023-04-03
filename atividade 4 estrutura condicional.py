hora: int
hora = int(input("digite uma hora do dia: "))
if hora < 12:
    print("Bom dia")
elif hora < 18:
    print("boa tarde")
else:
    print("boa noite")
