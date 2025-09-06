# Usando a biblioteca loggin para controlar as execuções da automação
import logging

# Definindo as configurações do loggin
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

my_logger = logging.getLogger(__name__) # contém o nome do módulo atual