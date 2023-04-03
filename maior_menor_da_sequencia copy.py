i = 1
lista = []

while i <= 5:
    user = float(input(f'Digite o peso da {i}° pessoa:'))
    lista.append(user)
    i += 1
print(lista)

maximo = max(lista)
minimo = min(lista)
indice = lista.index(maximo) + 1
indice2 = lista.index(minimo) + 1
print(f'O maior peso é da {indice}ª pessoa é {maximo}')
print(f'O maior peso é da {indice2}ª pessoa é {minimo}')
