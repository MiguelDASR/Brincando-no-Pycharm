#v = float(input('Qual o preço do produto? R$'))
#p = v * 5 / 100
#d = v - p
#print('O produto que custava R${} na promoção com o desconto  de 5% vai custar R${:.2f}'.format(v, d))
preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custavas R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))