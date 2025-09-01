import pyautogui as pg #biblioteca para controlar as ações com o mouse e teclado

pg.hotkey('win') # abre o menu iniciar

pg.typewrite('cmd') # digita 'cmd'

pg.press('enter') # pressiona enter

pg.sleep(2) # # espera por 2 segundos

pg.typewrite('start chrome') # digita o comando para abrir

pg.press('enter') # pressiona enter

pg.sleep(2) # espera 2 segundos

pg.typewrite('https://google.com/') # digita dentro do navegador para entrar no google

pg.press('enter') # pressiona enter

pg.sleep(3) # espera dois segundos

pg.typewrite('Dolar') # pesquisa dolar

pg.press('enter') # pressiona enter