# Questão 4 - países.

def calcular_anos(populacao_A, populacao_B, taxa_A, taxa_B):
    anos = 0
    while populacao_A < populacao_B:
        populacao_A += populacao_A * taxa_A
        populacao_B += populacao_B * taxa_B
        anos += 1
    return anos
anos_necessarios = calcular_anos(80000, 200000, 0.03, 0.015)
print(f"Serão necessários {anos_necessarios} anos.")