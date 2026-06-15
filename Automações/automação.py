import pyautogui as py
import time

py.FAILSAFE = False # desabilita o recurso de segurança que estava dando erro
delay_cliques = 3 # delay entre cada função

py.click(698, 1055)
time.sleep(delay_cliques)

py.click(428,387)
time.sleep(delay_cliques)

for essencia in range (45): # tudo o que estiver aqui entra em loop até completarem 45x 

    py.click(941,594)
    py.press('PgDn')
    time.sleep(delay_cliques)

    py.click(1253, 749)
    time.sleep(delay_cliques)

    py.click(1044, 666)
    time.sleep(delay_cliques)

    py.click(1042, 825)
    time.sleep(delay_cliques)