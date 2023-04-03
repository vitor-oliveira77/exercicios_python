name = input('Digite seu nome completo: \n')
name_separated = name.replace(" ", "")
first_name = name.split(' ')[0]
print('Analisando seu nome...\n')
print(f'Seu nome em maiúscula é', name.upper())
print(f'Seu nome em minusculo é', name.lower())
print('Seu nome tem ao todo:', len(name_separated), 'letras')
print(f'Seu primeiro nome é {first_name}', 'e tem', len(first_name), 'letras')
