import pyautogui as pg

print(pg.position()) # printar a posicao

# move o mouse para as coordenadas
pg.moveTo(x=2930, y=1598)
pg.click(x=2930, y=1598)

pg.typewrite("cmd") # pesquisar 'cmd'

pg.sleep(2) # esperar 2 segundos

pg.click(x=3107, y=744) # clicar nessas coordenadas