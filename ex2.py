nome = input('Digite seu nome: ') 
idade = input('digite sua idade: ')

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    
    if " " in nome:
        print(f'Seu nome contém espaços') 
    else: 
        print('Seu nome NÃO contém espaços')
    
    print(f'sua idade é {idade}')
    print(f'Seu nome contém {len(nome)}')   
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
    
else:
    print("Desculpe,você deixou campos vazios")


 

