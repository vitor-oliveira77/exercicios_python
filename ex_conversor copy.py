value_portfolio = float(input('Quanto você possui na cateira? R$ \n'))

value_dolar = value_portfolio / 5.28


print('Com R${:.2f} você pode comprar US${:.2f}'.format(
    value_portfolio, value_dolar))
