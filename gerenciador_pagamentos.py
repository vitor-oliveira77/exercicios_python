total_price = float(input('valor total das compras: '))

print(' [1] á vista dinheiro \n [2] á vista cartão \n [3] 2x no cartão \n [4] 3x ou mais no cartão')
option = input('Qual é a opção? ')


if option == '1':
    new_price = total_price - total_price * 0.15

if option == '2':
    new_price = total_price - total_price * 0.5

if option == '3':
    new_price = total_price / 2
    print(
        f'Sua compra de {total_price:.2f} vai ser dividida em 2x de {new_price}')

if option == '4':
    new_price = total_price + total_price * 0.20
    qtd_parcel = int(input('Quantidade de parcelas:'))
    split_price = new_price / qtd_parcel

    print(
        f'Sua compra de {total_price:.2f} vai ser dividida em {qtd_parcel} de {split_price}')

print(f'Sua compra de {total_price:.2f} vai custar {new_price:.2f}')
