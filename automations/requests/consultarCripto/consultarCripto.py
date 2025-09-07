import os
from dotenv import load_dotenv
import requests
import logging

# Importando a configuração de logging do arquivo separad
from log_config import LOGGING_CONFIG

# Aplica a configuração no início do script
logging.config.dictConfig(LOGGING_CONFIG)

# Pegar os loggers que foram configurados
logger_app = logging.getLogger('app')
logger_requisicao = logging.getLogger('requisicao')

# Função para requisição à API
def get_value_cripto (nome_moeda):
    # Carregando a variável de ambiente do arquivo .env
    load_dotenv()

    # Acesando a chave API
    api_key = os.getenv('COINGECKO_API_KEY')

    if api_key is None:
        logger_requisicao.error("Não foi possível encontrar a chave API. Verifique seu arquivo .env")
        return None

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

        # Verificar o status da requisição, se não foi, cai na excessão de conexão
        response.raise_for_status()

        # Se a requisição foi um sucesso, se não, ele cai na excessão de JSON
        data = response.json()

        # Log de sucesso
        logger_requisicao.info("Requisição API bem-sucedida.")

        # Retornar os dados
        return data
    
    except requests.exceptions.ConnectionError:
        logger_requisicao.error("Não foi possível fazer a conexão à API. Verifique sua internet.")
        return None
    
    except requests.exceptions.JSONDecodeError:
        logger_requisicao.error("Erro: A resposta da API não é um JSON válido.")
        return None

# Moeda de exemplo (Entrada da aplicação)
moeda = 'bitcoin'

# Log da aplicação antes da chamada
logger_app.info("Iniciando a busca pelo valor de %s.", moeda)

# Chamada da função
dados_result = get_value_cripto(moeda)

if dados_result:
    logger_app.info("Valor obtido com sucesso: {}" .format(dados_result))
else:
    logger_app.error("Falha ao obter valor: {}" .format(moeda))