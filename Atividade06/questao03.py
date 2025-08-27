"""3 - 

Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido 
pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade 
e estado correspondentes ao CEP consultado. 
"""

import requests

def obter_endereco_por_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        if "erro" in dados:
            return "CEP não encontrado."
        return f"""
            Estado: {dados['uf']}
            Cidade: {dados['localidade']}
            Bairro: {dados['bairro']}
            Logradouro: {dados['logradouro']}           
            
            
        """
    except requests.RequestException as e:
        return f"Erro ao obter o endereço: {e}"
    
cep = input("Digite o CEP para consulta (somente números): ")
endereco = obter_endereco_por_cep(cep)
print(endereco) 