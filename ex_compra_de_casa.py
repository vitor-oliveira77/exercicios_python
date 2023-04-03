value_house = float(input('Digite o valor da casa:'))
payday = float(input('Digite o salário:'))
years = int(input('Digite a quantidade de anos que será financiado:'))

years = years * 12

parcela = value_house / years

limit = payday * 0.3

if parcela > limit:
    print('Empréstimo negado')

if parcela <= limit:
    print('Empréstimo aprovado')
