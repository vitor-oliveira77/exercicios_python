numero1 = int(input("Digite o primeiro Numero: "))
numero2 = int(input("Digite o segundo Numero: "))
numero3 = int(input("Digite o terceiro numero: "))

if numero1 < numero2 and numero1 < numero3:
    menor = numero1
elif numero2 < numero3:
    menor = numero2
else:
    menor = numero3

print(f"Menor: {menor}")