# Questão 6 - salário. 

salario = 1000.00
aumento = 0.015

for ano in range(1996,2025):
  salario += salario * aumento
  aumento *= 2

print(f"em 2025 será: R$ {salario:.2f}")