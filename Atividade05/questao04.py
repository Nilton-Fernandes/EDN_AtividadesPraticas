"""4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia."""

import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade * 365


ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_em_dias = calcular_idade_em_dias(ano_nascimento)
print(f"A idade em dias é aproximadamente: {idade_em_dias} dias")
    
