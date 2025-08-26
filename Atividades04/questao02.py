"""
2 - Criar um código que registre as notas de alunos e calcular a média da turma."""

notas = []

while True:
    try:
        entrada = input("Digite uma nota (0 a 10) ou 's' para encerrar: ")
        
        if entrada.lower() == 's':
            break
        
        nota = float(entrada)
        
        if nota < 0 or nota > 10:
             raise Exception()
        
        notas.append(nota)
        

    except ValueError:
        print("Erro: as notas devem ser números!")
    except Exception:
        print("Erro: as notas devem ser números entre 0 e 10")

soma = 0
if len(notas) > 0:
    for nota in notas:
        soma += nota

    media = soma / len(notas)
    print("A média das notas é:", media)

else:
     print("Nenhuma nota foi inserida!")
