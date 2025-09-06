# Importando bibliotecas necessárias
import requests

# Função para consultar uma API do VIADEP para obter informações sobre um determinado CEP
def obter_endereco_por_cep (cep):
    # Validação inicial do CEP
    if not isinstance(cep, str) or not cep.isdigit() or len(cep) != 8:
        return "Erro: O CEP deve ser uma string de 8 dígitos."

    # Endpoint
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        # Envia um requisição GET para a 'url', o resultado é armazenado na variável 'response'
        response = requests.get(url)

        # Verifica o status da requisição GET (se retornar um código de erro, ele vai para o except)
        response.raise_for_status()

        # Se a requisição foi um sucesso, ele converte a string JSON em dicionário python
        dados = response.json()

        # Se o CEP não for válido, ele retorna um JSON com a chave 'erro'
        if 'erro' in dados and dados['erro'] is True:
            return "CEP não encontrado!"
        
        # Se tudo ocorre bem, retorna o dicionário com os dados
        return dados
    
    except requests.exceptions.RequestException as e:
        return f"Erro de conexão: {e}"
    except requests.exceptions.JSONDecodeError:
        return "Erro: A resposta da API não é um JSON válido."

# CEP para exemplo de requisição
cep_exemplo = '86047725'

# Utiliza a função para obter as informações do CEP
endereco_resultado = obter_endereco_por_cep(cep_exemplo)

# Exibe o endereço
print(endereco_resultado)