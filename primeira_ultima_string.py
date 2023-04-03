frase = input('Digite uma frase:').strip(' ')
quantidade = (len(frase))
qtd_letra = frase.count('a')
primeira_letra = frase.find('a') + 1
ultima_letra = frase.rfind('a') + 1

print(f'A frase possui {quantidade} letras ')
if qtd_letra < 1:
    print('Não possui está letra na frase.')
else:
    print(f'A primeira letra A se encontra na posição {primeira_letra}')
    print(f'A ultima letra A se encontra na posição {ultima_letra}')
