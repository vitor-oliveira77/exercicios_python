# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [1, 2, 3, 4]


soma_listas = [numero1 + numero2 for numero1, numero2 in zip(l1, l2)]
print(soma_listas)


# solução para qualquer linguagem (sem recursos python)

lista_soma = []

for i in range(len(l2)):
    lista_soma.append(l1[i] + l2[i])

print(lista_soma)
