import pyautogui as pg
import time

pg.press('win') #mousePosition.hotkey('win', 'r'), vai pressionar a tecla windows

time.sleep(2) # espera 2 segundos

pg.typewrite('notepad', interval=0.1) # escrever 'notepad'

time.sleep(2) # esperar 2 segundos

pg.press('enter') # pressiona enter

time.sleep(3) # espera 3 segundos

pg.typewrite("Ola, meu nome e Heitor, e estou cursando Analise e Desenvolvimento de Sistemas", interval=0.3) # escreve na tela

fecharJanelaNotepad = pg.getActiveWindow() # pega a janela que esta ativa

fecharJanelaNotepad.close() # fecha a janela ativa