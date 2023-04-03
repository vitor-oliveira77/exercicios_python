x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

if x > y:
    troca = x
    x = y
    y = troca

soma = 0
for i in range(x+1, y):
    if i % 2 != 0:
        soma = soma + i

print(f"Soma dos impares = {soma}")
