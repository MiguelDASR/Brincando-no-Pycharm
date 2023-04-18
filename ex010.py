d = float(input('Qanto dinheiro você tem na carteira? R$'))
c = d / 3.27
e = d / 4.57
i = d / 2.70
print('Com o valor de R${:.2f} você consegue comprar: \nUS${:.2f}\n€{:.2f}\n¥{:.2f}'.format(d, c, e, i))
print('Lembrando que a cotação atual do Dolar é de R$3.27, Euro R$4.57 e Yenes R$2.70.')
