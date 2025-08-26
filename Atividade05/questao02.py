"""2-  Crie uma função que verifique se uma palavra ou frase é um 
palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação).
 Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”."""

def eh_palindromo(texto):
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    
  
    invertido = ''
    for letra in texto_limpo:
        invertido = letra + invertido

   
    if texto_limpo == invertido:
        return "Sim"
    else:
        return "Não"
    

#main
    
texto = input("Digite uma palavra ou frase: ")
resultado = eh_palindromo(texto)
print(f"É palíndromo? {resultado}")


