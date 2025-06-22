import pyautogui as pg
import time

pg.press('win') #mousePosition.hotkey('win', 'r')

time.sleep(2)

pg.typewrite('notepad', interval=0.1)

time.sleep(2)

pg.press('enter')

time.sleep(3)

pg.typewrite("Ola, meu nome é Heitor, e estou cursando Analise e Desenvolvimento de Sistemas", interval=0.1)

# pegar a jenela que esta ativa
fecharJanelaNotepad = pg.getActiveWindow()

# fecha a janela ativa
fecharJanelaNotepad.close()