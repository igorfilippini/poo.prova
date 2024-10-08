# Questão 7 - dívida.

def tabela_divida(valor_divida):
    print("dívida | juros |   parcelas | valor Parcela")


    for parcelas, percentual_juros in [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]:
        juros = valor_divida * percentual_juros / 100
        valor_total = valor_divida + juros
        valor_parcela = valor_total / parcelas
        print(f"R${valor_total:.2f}  R${juros:.2f}{parcelas:13}   R${valor_parcela:.2f}")

valor = float(input("digite o valor da dívida: R$ "))
tabela_divida(valor)