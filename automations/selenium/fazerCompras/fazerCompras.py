# Para trabalhar com as paginas web
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

# Para melhorar a compatibilidade
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Usando o 'By' para trabalhar com atualizações mais recentes
from selenium.webdriver.common.by import By

# Importações para as esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Usando o pyautogui para burlar a seguranca da senha e salvar as informacoes
import pyautogui as pg

# Usar a biblioteca time para controlar o dellay
import time

# Importando o logging configurado
from logger import my_logger

# Função para pegar o 'driver'
def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Abrir o site
    driver.get('https://www.saucedemo.com/?utm_source=chatgpt.com')

    return driver

# Instanciando a função para pegar o 'driver'
driver = get_driver()

# Criar uma instância de espera explícita
wait = WebDriverWait(driver, 10) # espera por até 10 segundos

# Pesquisando e escrevendo nos elementos
wait.until(EC.visibility_of_element_located((By.NAME, 'user-name'))).send_keys('standard_user')
wait.until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys('secret_sauce')

# Apertando ENTER para entrar no site
wait.until(EC.element_to_be_clickable((By.NAME, 'login-button'))).click()

my_logger.debug("Informações preenchidas corretamente.")

# Tempo para o computador processar as informacoes
time.sleep(2)

# Identificar o botao e aperta-lo
x = 1063
y = 560

pg.click(x, y)

# Tempo para o computador processar as informacoes
time.sleep(2)

# Adicionar itens na sacola
wait.until(EC.visibility_of_element_located((By.NAME, 'add-to-cart-sauce-labs-backpack'))).click()
wait.until(EC.visibility_of_element_located((By.NAME, 'add-to-cart-sauce-labs-bike-light'))).click()

my_logger.debug("Itens adicionados à sacola.")

# Clicar na sacola
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()

my_logger.debug("Carrinho finalizado.")

# Encontrar o botao de checkout
wait.until(EC.visibility_of_element_located((By.NAME, 'checkout'))).click()

# Preenchendo formulario
wait.until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys('Heitor')
wait.until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys('Villa')
wait.until(EC.visibility_of_element_located((By.NAME, 'postalCode'))).send_keys('email')

my_logger.debug("Informações inseridas no formulário")

# Clicando em continuar para finalizar a compra
wait.until(EC.visibility_of_element_located((By.NAME, 'continue'))).click()

my_logger.debug("Informações corretamente inseridas pelo usuário.")

# Pegando todas as informacoes da compra
itens = {}

item1 = wait.until(EC.visibility_of_element_located((By.ID, 'item_4_title_link'))).text
valor1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div'))).text.replace('$', '')
item2 = wait.until(EC.visibility_of_element_located((By.ID, 'item_0_title_link'))).text
valor2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div'))).text.replace('$', '')

itens[item1] = valor1
itens[item2] = valor2

# Clicando no botao de finalizar o pedido
wait.until(EC.visibility_of_element_located((By.NAME, 'finish'))).click()

my_logger.debug("Compra finalizada.")


# Salvar as informacoes dentro do notepad

# Pressionar para abrir o executar do windows
pg.press('win')

# Tempo para o computador processar as informacoes
time.sleep(1)

# Digital notepad no executar do windows
pg.write("notepad", interval=0.1)

# Tempo para o computador processar as informacoes
time.sleep(1)

# Pressionar enter para prosseguir
pg.press('enter')

# Tempo para o computador processar as informacoes
time.sleep(1)

# Escrever a compra realizada
for item, valor in itens.items():
    # Converta o valor para string para que o pg.write() possa escrever
    valor_texto = str(valor)

    # Escreve o nome do item e o valor em uma nova linha
    pg.write(f'{item} - {valor_texto}', interval=0.05)

    # Pressionar o enter para pular um linha
    pg.press('enter')

    # Tempo para o computador processar as informacoes
    time.sleep(0.5)

driver.quit()