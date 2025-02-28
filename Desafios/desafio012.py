produto=float(input('Valor do produto:'))
porcentagem_desconto=float(input('Valor do desconto:'))
porcentagem_desconto = produto - (produto / 100 * porcentagem_desconto)
print('O valor do Produto é {} e com 5% de desconto fica {}'.format(produto, porcentagem_desconto))