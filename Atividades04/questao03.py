"""3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número."""

while True:
    try:
        senha = input("Digite a senha: ou \'s', para sair:".upper())
        if senha.upper() == "S":
            print("Saindo do programa: ")
            break
        if len(senha) < 8:
            raise Exception("A senha deve ter no mínimo 8 caracteres")
    
        tem_numero =  any(c.isdigit() for c in senha)
        tem_mauiscula = any(c.isupper() for c in senha)
        tem_minuscula = any(c.islower() for c in senha)

        if not (tem_numero and tem_mauiscula  and tem_minuscula ):
            raise Exception("A senha precisa conter letra \'minúscula, Maiuscula e número': ")
    
        print(f"{senha}: Senha forte: ")
        break
        
        
    except Exception as e:
        print(f"{senha}: Senha fraca: ", e)