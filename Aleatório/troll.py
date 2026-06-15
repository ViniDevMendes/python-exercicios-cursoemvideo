import pyautogui as py
import time 
import random

time.sleep(5)

mensagens = ["Fala", "Irmão", "Como", "Você", "Tá", "Tu ta ficando maluco?", "Teste", "shjiadajidsj", "você é chata", "oii", "tchau"]
for i in range (50):
    msg = random.choice(mensagens)
    py.write(msg)
    py.press('enter')