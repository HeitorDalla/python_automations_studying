import pyautogui as pg
import pyautogui as opcao
import pygetwindow as gw

def abrir_janela ():
    pg.hotkey('win', 'r')
    pg.sleep(1)

def fechar_janela ():
    pegarJanela = gw.getActiveWindow()
    pegarJanela.close()
    return

opcao = pg.confirm('Clique na opção desejada: ', buttons=['Google', 'Edge', 'Firefox']) # dar as opcoes

if (opcao == 'Google'):
    
    abrir_janela()

    pg.write('chrome')

    pg.sleep(1)

    pg.press('enter')

    pg.sleep(2)

    pg.write("Eu abri o google com automacao!!!!", interval=0.1)

    pg.sleep(1)

    fechar_janela()

elif (opcao == 'Edge'):
    abrir_janela()

    pg.write('msedge')

    pg.sleep(1)

    pg.press('enter')

    pg.sleep(2)

    pg.write("Eu abri o edge com automacao!!!!", interval=0.1)

    fechar_janela()

else:
    abrir_janela()

    pg.write('firefox')

    pg.sleep(1)

    pg.press('enter')

    pg.sleep(2)

    pg.write("Eu abri o firefox com automacao!!!!", interval=0.1)

    fechar_janela()