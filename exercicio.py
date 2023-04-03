palavra = 'vitor' 
palavra_usuario = ''

while True:
    letra_escolhida = input('Digite uma letra: ')
    if len(letra_escolhida) > 1:
        print('digite apenas uma letra')
        continue
    if letra_escolhida in palavra:
        print('possui a letra')
        palavra_usuario += letra_escolhida
    else:
        print('nao possui a letra')

    if palavra_usuario == palavra:
        print('parabens')
        break
# for letra in palavra: 
#     if letra_escolhida == letra:
#         print('possui a letra') 
#         palavra_usuario.join(letra)
#         print(palavra_usuario)
#         break
#     else: 
#         print('Não possui está letra') 
#         break