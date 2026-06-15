import pyautogui as py
import time 

py.FAILSAFE = False
delay_click = 1
delay_click2 = 3

py.click(511,1061)
time.sleep(delay_click)
for lixo in range (50):
    py.click(302,230)
    time.sleep(delay_click)
    py.click(341,260)
    time.sleep(delay_click)
    py.click(430,229)
    time.sleep(delay_click2)