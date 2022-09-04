import threading
import fs
import time
import botoes
import pyautogui
global alarme
alarme=False


def escar():
    pyautogui.press('esc')
    print('escou')
def contar():
    inicial=time.time()
    for i in range(4):
        final=time.time()
        time.sleep(1)
        if alarme :
            print("alarmou")
            break
        elif final-inicial>3:           
            escar()
            break
def comeca_contagem():
    print("entrei")
    #alarme=False
    threading.Thread(target=contar).start()

iniciu=time.time()
print('antes')

comeca_contagem()
botoes.entrar()
alarme=True

print('depois')
for i in range((len(botoes.arq.SERVICO))):
    try:
        fs.rodar(i)
    except:
        time.sleep(1)
#fs.rodar(9)
finall=time.time()
print(finall-iniciu)
