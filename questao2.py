# Questão 2 -números pares e ímpares.

pares = 0
impares = 0
for i in range(10):
  numero = int(input('digite um número:'))
  if numero % 2 == 0:
    pares += 1
  else:
    impares += 1
print('{} números pares'.format(pares))
print('{} números ímpares'.format(impares))