# Questão 3 - números primos.

numero = int(input('digite um número:'))
primo = True
for i in range(2,numero):
  if numero % i == 0:
    primo = False
    break
if primo:
  print('{} é primo'.format(numero))
else:
  print('{} não é primo'.format(numero))