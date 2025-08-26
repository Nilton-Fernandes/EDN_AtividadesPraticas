"""1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/)."""

while True:
    try:
        numero1 = float(input("Digite o primeiro número: ")) 
        numero2 = float(input("Digite o primeiro número: ")) 
        operador = input("Digite a operação: (+, -, /, *):")

        if operador == "+":
            resultado = numero1 + numero2
        elif operador == "-":
            resultado = numero1 - numero2
        elif operador == "/":
            resultado = numero1 / numero2
        elif operador == "*":
            resultado = numero1 - numero2
        else:
            raise Exception()    
        print(f"{numero1} {operador} {numero2} = {resultado:.2f}")
        break
        
    except ValueError:
        print("Você deve digitar apena números:")
    except ZeroDivisionError:
        print("Não é possível divisão por zero:")
    except Exception:
        print("Você deve usar somente essas operações: (+, -, /, *)")