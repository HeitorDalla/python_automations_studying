# Importando bibliotecas necessárias
import http.client # fornece a funcionalidade de cliente http para python, permitindo fazer requisições a servidore web
import json # fornece métodos para trabalhar com dados no formato json

# Função para consultar uma API do VIADEP para obter informações sobre um determinado CEP
def obter_endereco_por_cep (cep):
    # Cria a conexão HTTPS com o servidor 'viacep.com.br'
    conexao = http.client.HTTPConnection('viacep.com.br')

    # Envia uma requisição GET ao servidor ViaCEP
    conexao.request('GET', f"/ws/{cep}/json/")
   
    # Armazena a resposta do servidor
    resposta = conexao.getresponse()

    # lê o conteúdo completo da resposta (que é enviado pelo servidor em formato de bytes) até que todos os dados sejam recebidos
    dados = resposta.read()

    # Decodifica os bytes e o 'loads' converte a string JSON em dicionário python
    endereco = json.loads(dados.decode("utf-8"))

    # Encerra a conexão HTTPS com o servidor
    conexao.close()

    # Verifica se esta 'erro' no dicionário
    if "erro" not in endereco:
        return endereco
    else:
        return "CEP não encontrado!"

# CEP para exemplo de requisição
cep_exemplo = '01001000'

# Utiliza a função para obter as informações do CEP
endereco_resultado = obter_endereco_por_cep(cep_exemplo)

# Exibe o endereço
print(endereco_resultado)