import logging.config

LOGGING_CONFIG = {
    'version': 1, # versão do esquema de configuração
    'disable_existing_loggers': False, # define se os loggers que existiam antes dessa configuração serão desativados, manter como falso
    'formatters': {
        'standard': { # nome do formato
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s', # string que define o layout do log (data e hora, nome do logger, nivel e mensagem)
            'datefmt': '%Y-%m-%d %H:%M:%S' # formato específico da data e hora
        },
    },
    'handlers': { # define para onde as mensagens serão enviadas (cada handler tem um destino diferente)
        'console': {
            'class': 'logging.StreamHandler', # envia as mensagens para a saída padrão (console)
            'formatter': 'standard', # usa o modelo de formato definido antes
            'level': 'DEBUG', # define o nível, esse handler só processará mensagens DEBUG ou superior
        },
        'requisicao_file': { 
            'class': 'logging.FileHandler', # salva as mensagens em um arquivo
            'formatter': 'standard', # usa o modelo de formato definido antes
            'filename': 'logs/requisicao.log', # nome do arquivo onde os logs serão salvos
            'level': 'INFO', # define o nível, esse handler só processará mensagens INFO ou superior
        },
        'app_file': { # nome do logger
            'class': 'logging.FileHandler', # salva as mensagens em um arquivo
            'formatter': 'standard', # usa o modelo de formato definido antes
            'filename': 'logs/app.log', # nome do arquivo onde os logs serão salvos
            'level': 'DEBUG', # define o nível, esse handler só processará mensagens DEBUG ou superior
        }
    },
    'loggers': { # define os loggers, ou seja, quais loggers usarão quais handlers e em qual nível
        '': {  # Logger raiz (root)
            'handlers': ['console'], # usa apenas o handler 'console'
            'level': 'DEBUG', # seu nível mínimo de processamento é DEBUG
            'propagate': True, # as mensagens de seus loggers filhos serão passadas para ele (padrão)
        },
        'requisicao': {
            'handlers': ['requisicao_file'], # usa apenas o handler 'requisicao_file'
            'level': 'INFO', # seu nível mínimo de processamento é INFO
            'propagate': False, # impede que as mensagens deste logger sejam enviadas para o logger raiz (console), evitando logs duplicados no console.
        },
        'app': {
            'handlers': ['app_file'], # usa apenas o handler 'app_file'
            'level': 'DEBUG', # seu nível mínimo de processamento é DEBUG
            'propagate': False, # impede que as mensagens deste logger sejam enviadas para o logger raiz (console), evitando logs duplicados no console.
        }
    }
}

"""

Jeito manual de fazer a configuração dos loggers e handlers:

# Definindo as configurações do loggin
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler()
    ]
)

# Criando logger e handler para a 'requisição'
logger_requisicao = logging.getLogger('requisicao')
logger_requisicao.setLevel(logging.INFO)
logger_requisicao.propagate = False # Desativa a propagação para evitar que os logs de requisição
# sejam duplicados no handler do root logger

requisicao_handler = logging.FileHandler('requisicao.log')
requisicao_handler.setLevel(logging.INFO)

logger_requisicao.addHandler(requisicao_handler)

# Criando logger e handler para o 'app'
logger_app = logging.getLogger('app')
logger_app.setLevel(logging.DEBUG)
logger_app.propagate = False # Desativa a propagação para evitar que os logs de requisição
# sejam duplicados no handler do root logger

app_handler = logging.FileHandler('app.log')
app_handler.setLevel(logging.DEBUG)

logger_app.addHandler(app_handler) 

"""