# Questão 5 - tabela. 

def gerar_tabela():
  print("quantidade - preço")
  for i in range(1,21):
    print("{} - R${:.2f}".format(i,i*0.12))
gerar_tabela()