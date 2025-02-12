# código para rodar no terminal para instalar as Bibliotecas utilizadas:
# pip install pyautogui
# pip install pandas openpyx

import pyautogui
from time import sleep
import pandas as pd

pyautogui.PAUSE = 1

sleep(3)

# Acessar o navegador
pyautogui.press('win')
navegador = 'Microsoft Edge'
pyautogui.write(navegador)
pyautogui.press('enter')    

sleep(3)

# Informar o site
link = 'https://gabrielrobertooliveira.github.io/cadastro-simples/'
pyautogui.write(link)
pyautogui.press('enter')

sleep(3)

# Efetuar Login
pyautogui.click(x=536, y=387)
pyautogui.write('usuario@gmail.com')
pyautogui.press('tab')
pyautogui.write('admin123')
pyautogui.press('tab')
pyautogui.press('enter')

# Vincular a tabela a uma variável
tabela = pd.read_csv('itens.csv')
sleep(2)

# Iniciar cadastro dos itens
for linha in tabela.index:

    nome = str(tabela.loc[linha, 'nome']) 
    tipo = str(tabela.loc[linha, 'tipo'])
    qtn = str(tabela.loc[linha, 'quantidade'])
    obs = str(tabela.loc[linha, 'obs'])

    pyautogui.click(x=534, y=230)

    pyautogui.write(nome)
    pyautogui.press('tab')
    pyautogui.write(tipo)
    pyautogui.press('tab')
    pyautogui.write(qtn)
    pyautogui.press('tab')
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(1000)
    