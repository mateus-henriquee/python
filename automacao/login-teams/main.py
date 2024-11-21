# LOGIN - MICROSOFT TEAMS

import pyautogui as pa
import time


pa.PAUSE = 0.75

#COMANDOS PARA INICIAR GOOGLE CHROME E TEAMS
    pa.press('win')
    pa.write('Google Chrome')
    pa.press('enter')
    pa.write("https://teams.microsoft.com/v2/")
    pa.press('enter')


#TELA DE LOGIN
    time.sleep(9.25)
    pa.write("meulogin@gmai.co")
    pa.press('enter')
    time.sleep(3)
    pa.write("minhasenha123")
    pa.press('enter')