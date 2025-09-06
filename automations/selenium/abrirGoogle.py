from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# O ChromeDriver será baixado e gerenciado automaticamente
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abrir o Google
driver.get('https://www.google.com')

time.sleep(3)
driver.quit()