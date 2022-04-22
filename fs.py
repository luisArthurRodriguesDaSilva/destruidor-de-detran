import botoes
from selenium import webdriver
import threading
import pandas as pd
#from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import fs
import time
import json
import botoes
import pyautogui
#--------------------alarmes--------------------------------------#
def escar():
    pyautogui.press('esc')
    print('escou1')
def contar():
    global alarme1
    alarme1=False
    inicial=time.time()
    for i in range(4):
        final=time.time()
        time.sleep(1)
        if alarme1 :
            print("alarmou1")
            break
        elif final-inicial>3:
            escar()
            break
def comeca_contagem():
    print("entrei1")
    time.sleep(1)
    threading.Thread(target=contar).start()
#################-----------------------------------------------------------

def segunda_via_crv(a):             #feito
    botoes.bot_segunda_via_crv()
    time.sleep(2)
    botoes.procedimento_padrao_2crv(a)


def pri_lic(a):                     #feito
    botoes.procedimento_padrao_pri_lic(a)

def itpve(a):                       #feito
    botoes.procedimento_padrao_(a)
    time.sleep(1)

def tp(a):                  #feito
    botoes.bot_tp(a)
    time.sleep(1)
    botoes.procedimento_padrao_tp(a)



def tpm(a):             #feito
    botoes.bot_tpm(a)
    print("passei do bot")
    time.sleep(1)
    botoes.procedimento_padrao_tpm(a)

def tj(a):                              #'feita
    botoes.bot_transferencia_de_juris(a)
    time.sleep(1)
    botoes.procedimento_padrao_tj(a)
#-----------------------------------------------------------------------------------------------------
def alt_carac(a):


    time.sleep(1)

def t_plac(a):                  #feito
    botoes.bot_t_plac(a)
    time.sleep(1)
    botoes.procedimento_padrao_t_plac(a)

def BX_GR(a):
    botoes.bot_BX_GR(a)
    time.sleep(1)
    botoes.procedimento_padrao_BX_GR(a)

def BV(a):
    time.sleep(1)

def primeira_palavra(palavra):
    if '/' not in palavra:
        return palavra
    else:
        for i in range(len(palavra)):
            print(f"{i}--{palavra}")
            if palavra[i]=='/':
                print(palavra[0:i])
                break
        return (palavra[0:i])
def abrir(a):
    if a>0 :
        botoes.aba+=1
        botoes.abrir_outra(a,botoes.aba)

def rodar(a):
    global alarme1
    comeca_contagem()
    abrir(a)
    alarme1=True
    try:
        z=x[primeira_palavra(botoes.arq.SERVIÇO[a])]
        print(f"{z}z")
        time.sleep(1)
        comeca_contagem()
        ini = time.time()
        botoes.nav.find_element(By.XPATH, f'/html/body/div[5]/div[5]/div/div[2]/ul/li[{str(z)}]/a').click()  ####
        print(f"{time.time() - ini}ihhhh ")
        alarme1 = True
        print(f"cheguei,serviço {a}")
        if z == 1:
            pri_lic(a)
        elif z == 2:
            tp(a)
        elif z == 3:
            itpve(a)
        elif z == 4:
            tpm(a)
        elif z == 5:
            tj(a)
        elif z == 6:
            alt_carac(a)
        elif z == 7:
            t_plac(a)
        elif z == 8:
            segunda_via_crv(a)
        elif z == 9:
            BX_GR(a)
        elif z == 10:
            BV(a)
    except Exception as e:
        print(f"falhou em z--{a}{z}")
        print (e)

    #botoes.nav.find_element(By.CSS_SELECTOR,".recaptcha-checkbox-border[role=presentation]").click()


x={
    '1 LIC'         :   1,
    'TP'            :   2,
    'itpve'         :   3,
    'TPM'           :   4,
    'TJ'            :   5,
    'alt carac'     :   6,
    'PL MERCOSUL'   :   7,
    '2 VIA CRV'     :   8,
    'BX GR'         :   9,
    'BV'            :   10,
}
if __name__ == "__main__":
    comeca_contagem()
    time.sleep(2)
    print("a")
    alarme1=True