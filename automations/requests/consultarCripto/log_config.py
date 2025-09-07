import logging.config

LOGGING_CONFIG = {
    'version': 1, # versão do esquema de configuração
    'disable_existing_loggers': False, # define se os loggers que existiam antes dessa configuração serão desativados, manter como falso
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'DEBUG',
        },
        'requisicao_file': {
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': 'requisicao.log',
            'level': 'INFO',
        },
        'app_file': {
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': 'app.log',
            'level': 'DEBUG',
        }
    },
    'loggers': {
        '': {  # Logger raiz (root)
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'requisicao': {
            'handlers': ['requisicao_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'app': {
            'handlers': ['app_file'],
            'level': 'DEBUG',
            'propagate': False,
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

# Criando logger e handler para a requisição
logger_requisicao = logging.getLogger('requisicao')
logger_requisicao.setLevel(logging.INFO)
logger_requisicao.propagate = False # Desativa a propagação para evitar que os logs de requisição
# sejam duplicados no handler do root logger

requisicao_handler = logging.FileHandler('requisicao.log')
requisicao_handler.setLevel(logging.INFO)

logger_requisicao.addHandler(requisicao_handler)

# Criando logger e handler para o app
logger_app = logging.getLogger('app')
logger_app.setLevel(logging.DEBUG)
logger_app.propagate = False # Desativa a propagação para evitar que os logs de requisição
# sejam duplicados no handler do root logger

app_handler = logging.FileHandler('app.log')
app_handler.setLevel(logging.DEBUG)

logger_app.addHandler(app_handler) 

"""