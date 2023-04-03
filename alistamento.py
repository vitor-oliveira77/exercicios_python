from datetime import date
current = date.today().year

year_born = int(input('Digite o ano de nascimento: '))
age = current - year_born

if age == 18:
    print('Você precisa se alistar imediatamente!')
elif age > 18:
    x = age - 18
    print(f'Você deveria ter se alistado á {x} anos')
elif age < 18:
    x = age - 18
    print(f'Você só se alistará daqui a {x} anos')
