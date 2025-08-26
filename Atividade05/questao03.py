"""3 - Crie um programa que serve para calcular o preço final de um produto após aplicar 
um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado."""

def calcular_desconto(preco, porcentagem_desconto):
    desconto = preco * (porcentagem_desconto / 100)
    preco_final = preco - desconto
    return round(preco_final, 2)    

#main
preco = float(input("Digite o preço do produto: R$ "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))   
preco_com_desconto = calcular_desconto(preco, porcentagem_desconto)
print(f"O preço final com desconto é: R$ {preco_com_desconto}")     
