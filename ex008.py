m = float(input('A distância em metros: '))
km = m / 1000
hm = m / 100
dm = m * 10
cm = m * 100
mm = m * 1000
print('A medida de {}m corresponde a:\n{:.0f}km\n{:.0f}hm\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(m, km, hm, dm, cm, mm))