import pyautogui as pg
import pygetwindow as gw

def abrir_janela ():
    pg.hotkey('win', 'r')
    pg.sleep(1)

def fechar_janela ():
    pegarJanela = gw.getActiveWindow()
    if pegarJanela is not None:
        pegarJanela.close()
    return

navegadores = {
    'Google': 'chrome',
    'Edge': 'msedge',
    'Firefox': 'firefox'
}

mensagens = {
    'Google': 'Eu abri o Google com automação!!!!',
    'Edge': 'Eu abri o Edge com automação!!!!',
    'Firefox': 'Eu abri o Firefox com automação!!!!'
}

opcao = pg.confirm('Clique na opção desejada: ', buttons=['Google', 'Edge', 'Firefox']) # dar as opcoes

if opcao in navegadores:
    abrir_janela()

    pg.write(navegadores[opcao])

    pg.sleep(1)

    pg.press('enter')

    pg.sleep(2)

    pg.write(mensagens[opcao], interval=0.1)

    pg.sleep(1)

    fechar_janela()