import os
from dotenv import load_dotenv
import requests
import logging

# Definindo as configurações do loggin
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Função para requisição à API
def get_value_cripto (nome_moeda):
    # Carregando a variável de ambiente do arquivo .env
    load_dotenv()

    # Acesando a chave API
    api_key = os.getenv('COINGECKO_API_KEY')

    if api_key is None:
        logging.error("Não foi possível encontrar a chave API.")
    else:
        endpoint = 'https://api.coingecko.com/api/v3/simple/price'

        # Parâmetros para passar para o endpoint
        params = {
            'ids': nome_moeda, # Parâmetro para o nome da moeda
            'vs_currencies': 'brl',
            'x_cg_demo_api_key': api_key  # Parâmetro para a chave
        }

        try:
            # Envia um requisição GET para a 'url', o resultado é armazenado na variável 'response'
            response = requests.get(endpoint, params=params)

            # Verificar o status da requisição
            response.raise_for_status()

            # Se a requisição foi um sucesso
            data = response.json()

            # Retornar os dados
            return data
        except requests.exceptions.ConnectionError:
            logging.error("Não foi possível fazer a conexão à API.")

# Moeda de exemplo
moeda = 'bitcoin'

# Chamada da função
dados_result = get_value_cripto(moeda)

# Logging para resultado
logging.debug(dados_result)