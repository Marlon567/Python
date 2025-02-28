salario=float(input('Valor do salário:'))
aumento=float(input('porcentagem de aumento:'))
total= salario + ( salario / 100 * aumento )
print('O salario de {} foi para {}'.format(salario, total))