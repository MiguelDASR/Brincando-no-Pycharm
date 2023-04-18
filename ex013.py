salário = float(input('Qual é o salário do funcionario? R$'))
almento = salário + (salário * 15 / 100)
print('O fUncionário que ganhava R${:.2f}, com 5% de aumento, passa a receber {:.2f}.'.format(salário, almento))
