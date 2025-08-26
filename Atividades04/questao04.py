"""4 - Criar um código que serve para analisar números digitados pelo usuário, 
classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos."""

pares = 0
impares = 0

while True:
    try:
        entrada =  input("Digite um número inteiro ou \'S' para sair: ".upper())

        if entrada.upper() == "S":
            break
        numero = int(entrada)

        if numero % 2 ==0:
            print(f"{numero} é par: ")
            pares += 1
        else:
            print(f"{numero} é impa: ")
            impares += 1

    except ValueError:
        print("O valor digitado não é um número inteiro: ")
    
print(f"\n{pares}: pares e {impares}: impares:")