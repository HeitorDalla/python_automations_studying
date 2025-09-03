# Objetivo: entrar no site com duas contas, ar


# Para trabalhar com as paginas web
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

# Para melhorar a compatibilidade
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Usando o 'By' para trabalhar com atualizações mais recentes
from selenium.webdriver.common.by import By

# Usando o pyautogui para burlar a seguranca da senha e salvar as informacoes
import pyautogui as pg

import time

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

# Abrir o site
driver.get('https://www.saucedemo.com/?utm_source=chatgpt.com')

# Tempo para o computador processar as informacoes
time.sleep(2)

# Pesquisando pelos elementos
username = driver.find_element(By.NAME, 'user-name')
password = driver.find_element(By.NAME, 'password')

# Escrevendo as informacoes
username.send_keys('standard_user')
password.send_keys('secret_sauce')

# Tempo para o computador processar as informacoes
time.sleep(2)

# Apertando ENTER para entrar no site
button_enter = driver.find_element(By.NAME, 'login-button')
button_enter.click()

# Tempo para o computador processar as informacoes
time.sleep(1)

# Identificar o botao e aperta-lo
x = 1063
y = 560

pg.click(x, y)

# Tempo para o computador processar as informacoes
time.sleep(2)

# Adicionar valores na sacola
compra1 = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack')
compra1.click()
compra2 = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-bike-light')
compra2.click()

# Tempo para o computador processar as informacoes
time.sleep(2)

# Clicar na sacola
sacola = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
sacola.click()

# Tempo para o computador processar as informacoes
time.sleep(2)

# Encontrar o botao de checkout
checkout = driver.find_element(By.NAME, 'checkout')
checkout.click()

# Tempo para o computador processar as informacoes
time.sleep(2)

# Preenchendo formulario
first_name = driver.find_element(By.NAME, 'firstName').send_keys('Heitor')
last_name = driver.find_element(By.NAME, 'lastName').send_keys('Villa')
code_postal = driver.find_element(By.NAME, 'postalCode').send_keys('email')

# Tempo para o computador processar as informacoes
time.sleep(2)

# Clicando em continuar para finalizar a compra
continuar = driver.find_element(By.NAME, 'continue')
continuar.click()

# Tempo para o computador processar as informacoes
time.sleep(2)

# Pegando todas as informacoes da compra
itens = {}

item1 = driver.find_element(By.ID, 'item_4_title_link').text
valor1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text.replace('$', '')
item2 = driver.find_element(By.ID, 'item_0_title_link').text
valor2 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div').text.replace('$', '')

itens[item1] = valor1
itens[item2] = valor2

# Clicando no botao de finalizar o pedido
finish = driver.find_element(By.NAME, 'finish')
finish.click()


# Salvar as informacoes dentro do notepad

# Pressionar para abrir o executar do windows
pg.press('win')

# Tempo para o computador processar as informacoes
time.sleep(2)

# Digital notepad no executar do windows
pg.write("notepad", interval=0.1)

# Tempo para o computador processar as informacoes
time.sleep(2)

# Pressionar enter para prosseguir
pg.press('enter')

# Tempo para o computador processar as informacoes
time.sleep(2)

# Escrever a compra realizada
for item, valor in itens.items():
    # Converta o valor para string para que o pg.write() possa escrever
    valor_texto = str(valor)

    # Escreve o nome do item e o valor em uma nova linha
    pg.write(f'{item} - {valor_texto}')

    # Pressionar o enter para pular um linha
    pg.press('enter')

    # Tempo para o computador processar as informacoes
    time.sleep(2)

driver.quit()