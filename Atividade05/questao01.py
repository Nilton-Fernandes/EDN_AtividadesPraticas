"""1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total
 da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e 
 na porcentagem desejada. 
 Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada"""

def calcular_gorjeta(valor_conta,porcentagem_gorgeta):
     gorgeta = valor_conta * (porcentagem_gorgeta/100)

     return round(gorgeta,2)

#main
total_conta = float(input("Digite o valor da conta: "))
porcentagem_gorgeta = float(input("Qual percentual de gorgerta? "))

valor_gorgeta = calcular_gorjeta(total_conta,porcentagem_gorgeta)
     
print(f"O valor da gorgeta é: R$ {valor_gorgeta}")
 