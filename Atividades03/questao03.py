"""3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""


unidade_de_origem = input("Digite a unidade de temperatura (C, F ou K): ").upper()

if unidade_de_origem not in ("C", "F", "K"):
    resultado = "Unidade de origem inválida!"
else:
    unidade_de_destino = input("Digite a unidade de destino (C, F ou K): ").upper()
    if unidade_de_destino not in ("C", "F", "K"):
        resultado = "Unidade de destino inválida!"
    else:
        temperatura = float(input("Digite a temperatura: "))

        if unidade_de_origem == unidade_de_destino:
            resultado = f"{temperatura:.2f} {unidade_de_destino}"

        elif unidade_de_origem == "C" and unidade_de_destino == "F":
            resultado = f"{(temperatura * 9/5) + 32:.2f} °F"

        elif unidade_de_origem == "C" and unidade_de_destino == "K":
            resultado = f"{temperatura + 273.15:.2f} K"

        elif unidade_de_origem == "F" and unidade_de_destino == "C":
            resultado = f"{(temperatura - 32) * 5/9:.2f} °C"
            
        elif unidade_de_origem == "F" and unidade_de_destino == "K":
            resultado = f"{((temperatura - 32) * 5/9) + 273.15:.2f} K"

        elif unidade_de_origem == "K" and unidade_de_destino == "C":
            resultado = f"{temperatura - 273.15:.2f} °C"
        else: 
            resultado = f"{((temperatura - 273.15) * 9/5) + 32:.2f} °F"

print("Resultado:", resultado)
