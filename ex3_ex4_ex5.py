#EXERCICIO 3
#numero_int = input('Digite um número inteiro:   '))

# entrada = input('Digite um número inteiro:  ')
# try: 
#     entrada_int = int(entrada) 
#     par_impar = entrada_int % 2 == 0 
#     par_impar_texto = 'impar'

#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#     print(f'Você não digitou um número inteiro')
#exercicio 4 

# horario = input(' Digite o horário:   ') 
# hora_int = int(horario)
# if hora_int >= 5 and hora_int < 12:
#     print('Bom Dia')
# elif hora_int >= 12 and hora_int < 18:
#     print('Boa Tarde') 
# elif hora_int >= 18:
#     print('Boa noite')


nome = input('Digite seu nome:   ')
tamanho_nome = len(nome)
if tamanho_nome > 1:
    if tamanho_nome <= 4: 
     print('Seu nome é muito curto')
    elif len(nome) == 5 or nome == 6:
        print('Seu nome é normal')
    else: 
        print('Seu nome é muito grande') 
else: 
    print('Digite mais de uma letra.')