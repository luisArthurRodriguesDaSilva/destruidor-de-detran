import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import threading
import possibilidades
import PySimpleGUI as sg
#-------------
import os
import sys

#--------------
global nav
global arq
global endereco


working_directory = os.getcwd()
sg.theme('LightBlue3')
layout = [
            [
                sg.Text('insira o endereço do arquivo'),
                sg.InputText(background_color='#ffffff'),
                sg.FileBrowse(
                    initial_folder=working_directory,
                    file_types=[("xmls Files", "*.xlsx")]
                    )
            ],
            [sg.Text('matricula'), sg.InputText(background_color='#ffffff')],
            [sg.Button('começar'), sg.Button('Cancelar')] ]

# Create the Window
#window = sg.Window('Auto-Detran', layout,icon='WIN_20210916_20_43_58_Pro.jpg')

window = sg.Window('Auto-Detran',icon=r"logo-removebg-preview.ico").Layout(layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel' or event ==('começar'): # if user closes window or clicks cancel
        endereco=input=values[0].replace('"','')
        matricula=values[1].replace('"','')
        break
    #print('You entered ', values[0])

window.close()


nav = webdriver.Chrome(ChromeDriverManager().install())
action=webdriver.ActionChains(nav)
nav.maximize_window()


#arq = pd.read_json(r"C:\Users\luarp\PycharmProjects\destruidor de detran\venv\dados do detran.json")
arq = pd.read_excel(f"{endereco}")
aba=0

def digitar(w):
    pyautogui.typewrite(f"{w}",interval=0.05)
def escar():
    pyautogui.press('esc')
    print('escou2')
def contar():
    global alarme2
    alarme2 = False
    inicial=time.time()
    for i in range(10):
        final=time.time()
        time.sleep(1)
        if alarme2 :
            print("alarmou2")
            break
        elif final-inicial>5:
            escar()
            break
def comeca_contagem():
    print("entrei2")
    time.sleep(1)
    threading.Thread(target=contar).start()
def abrir_outra(a,aba):
    nav.execute_script("window.open('https://www.detran.rj.gov.br/_documento.asp?cod=7620', '_blank')")
    nav.switch_to.window(nav.window_handles[aba])
def entrar():
    nav.get('https://www.detran.rj.gov.br/_documento.asp?cod=7620')
#--------------------------------------escbots---------------------------------------------------------------------------------------------------------
def escolher_botao_cpfcnpj_2crv(a) :
    if len(str(remover_traços(remover_pontos(arq['CPF/CNPJ'][a]))))<13:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[3]/div[1]/div[2]/input').click()
    else:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[3]/div[2]/div[2]/input').click()
def escolher_botao_cpfcnpj_tj(a) :
    if len(str(remover_traços(remover_pontos(arq['CPF/CNPJ'][a]))))<13:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/table[2]/tbody/tr[1]/td[1]/div/input[1]').click()
    else:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/table[2]/tbody/tr[1]/td[1]/div/input[2]').click()
def escolher_botao_cpfcnpj_tpm(a):
    if len(str(remover_traços(remover_pontos(arq['CPF/CNPJ'][a]))))<13:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[1]/div[1]/div[2]/input').click()
    else:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[1]/div[2]/div[2]/input').click()
def escolher_botao_cpfcnpj_pri_lic(a):
    if len(str(remover_traços(remover_pontos(arq['CPF/CNPJ'][a]))))<13:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[2]/div[1]/div[2]/input').click()
    else:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[2]/div[2]/div[2]/input').click()
def escolher_botao_cpfcnpj_tp(a):
    if len(str(remover_traços(remover_pontos(arq['CPF/CNPJ'][a]))))<13:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[5]/div[1]/div[2]/input').click()
    else:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[5]/div[2]/div[2]/input').click()
def escolher_botao_cpfcnpj_t_plac(a) :
    if len(str(remover_traços(remover_pontos(arq['CPF/CNPJ'][a]))))<13:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[3]/div[1]/div[2]/input').click()
    else:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[3]/div[2]/div[2]/input').click()
#-----------------------------------------------------------------------pps--------------------------------------------------------
def matricular():
    nav.find_element(By.ID, 'matriculaDespachante').send_keys(str(matricula))
def selecionar_serv_extra_tpm(a):
    palavras=separar_palavras(arq.SERVICO[a])
    for palavra in palavras:
        try:
            print(palavra)
            p=remover_barras(palavra)
            print(p)
            if p == 'BX GR':
                nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/ul[1]/li/input').click()
            else:
                tipo = possibilidades.extras_tpm[str(p)]
                print(tipo)
                nav.find_element(By.XPATH,f'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/ul[2]/li[{tipo}]/input').click()
        except Exception as e:
            print(e)
            print("falhou em 'selecionar_serv_extra_tpm'")
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
def procedimento_padrao(a):
    global alarme2
    try:
        nav.find_element(By.NAME, 'placa').send_keys(str(arq.PLACA[a]))
    except Exception as e:
        print(e)
        print("falhou em PLACA")
    try:
        nav.find_element(By.NAME, 'renavam').click()
        print((remover_pontos(str(arq.RENAVAN[a]))))
        print((remover_ultimo_zero(str(arq.RENAVAN[a]))))

        print((remover_ultimo_zero(remover_pontos(str(arq.RENAVAN[a])))))
        digitar(((remover_pontos(remover_ultimo_zero(str(arq.RENAVAN[a]))))))
    except Exception as e:
        print(e)
        print("falhou em RENAVAM")
    try:
        nav.find_element(By.NAME, 'cpf').send_keys(remover_traços(remover_pontos(str(arq['CPF/CNPJ'][a]))))
    except Exception as e:
        print(e)
        print("falhou em CPF")
    try:
        nav.find_element(By.NAME, 'duda').send_keys(str(arq.DUDA[a]))
    except Exception as e:
        print(e)
        print("falhou em DUDA")
    try:
        print("cepado0")
        nav.find_element(By.ID, 'cep').click()
        print("cepado")
        nav.find_element(By.ID, 'cep').send_keys(remover_traços(str(remover_traços(arq.CEP[a]))))
        print("cepado2")
    except Exception as e:
        print(e)
        print("falhou em CEP")
        print("falhou em CEP")
    if primeira_palavra(arq.SERVICO[a])== 'TP':
        try:
            print("AGORA")
            time.sleep(1)
            print(f"{filtro_pro_bug(str(arq['DATA REC'][a]))}")
            print(f"{str(arq['DATA REC'][a])}")
            print(f"{remover_traços(str(arq['DATA REC'][a]))}")
            alarme2 = True
            nav.find_element(By.NAME, 'data_venda').click()
            digitar(str(filtro_pro_bug(str(arq['DATA REC'][a]))))
            time.sleep(0.1)

        except Exception as e:
            print("falhou em data TP")
            print(e)
    else:
        try:
            print(777)
            nav.find_element(By.NAME,'data_venda').click()
            print(f"66{str(arq['DATA REC'][a])}")
            datas=separar_palavras_traco(str(arq['DATA REC'][a]))
            print (f"a data é{datas}")
            print(f"{remover_traços(datas[2])}/{remover_traços(datas[1])}/{remover_traços(datas[0])}")
            digitar(f"{remover_traços(datas[2][0:2])}/{remover_traços(datas[1])}/{remover_traços(datas[0])}")
            print(f"cheguei em else indevido)")#{arq.SERVICO[a]}")
        except Exception as e:
            print(e)
            print("falhou em data venda")
    try:
        nav.find_element(By.NAME,'crv').send_keys(str(arq.CRV[a]))
    except Exception as e:
        print(e)
        print("falhou em crv")
    try:
        nav.find_element(By.XPATH,f"/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/table[2]/tbody/tr[8]/td[2]/select/option[{str(possibilidades.uf_origem[arq.ESTADO[a]])}]").click()
    except Exception as e:
        print(e)
        print("falhou em UF")

    alarme2 = True
def procedimento_padrao_2crv(a):
    global alarme2
    comeca_contagem()
    procedimento_padrao(a)
    escolher_botao_cpfcnpj_2crv(a)
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/input[3]').send_keys(arq['CPF/CNPJ'][a])
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[1]/option[2]').click()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[2]/option[4]').click()
    matricular()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[7]/div[2]/div[2]/div[2]/input').click()
    alarme2=True
    #nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[7]/div[2]/div[2]/div[2]/input').click()
def procedimento_padrao_tj(a):
    global alarme2
    comeca_contagem()
    procedimento_padrao(a)
    escolher_botao_cpfcnpj_tj(a)
    #nav.find_element(By.XPATH,f"/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/table[2]/tbody/tr[8]/td[2]/select/option[{str(possibilidades_uf_origem['ES'])}]").click()

    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/table[2]/tbody/tr[9]/td[2]/input').send_keys(str(arq.CEP[a]))
    time.sleep(1)
    #A REVER---------------------------------------------------------------------------------------------------------------------------------
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/table[2]/tbody/tr[11]/td[2]/select/option[4]').click()   #|
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/table[2]/tbody/tr[12]/td[2]/select/option[2]').click()   #|
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/table[2]/tbody/tr[13]/td[2]/select/option[4]').click()   #|
    #----------------------------------------------------------------------------------------------------------------------------------------
    nav.find_element(By.XPATH,'//*[@id="despachante2"]/td[2]/div/input[2]').click()
    nav.find_element(By.XPATH, '//*[@id="exibeAceite"]').click()
    matricular()
    alarme2=True
def procedimento_padrao_tpm(a):
    global alarme2
    comeca_contagem()
    procedimento_padrao(a)
    escolher_botao_cpfcnpj_tpm(a)
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[1]/option[4]').click()#tipo/outros
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[2]/option[2]').click()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[3]/option[4]').click()
    time.sleep(1)
    nav.find_element(By.XPATH,'//*[@id="despachante"]/div[2]/div[2]/div[2]/input').click()
    matricular()
    alarme2=True
def procedimento_padrao_pri_lic(a):
    global alarme2
    comeca_contagem()
    procedimento_padrao(a)
    escolher_botao_cpfcnpj_pri_lic(a)
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[1]/option[5]').click()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[2]/option[2]').click()
    #parte incompreendida=============================
    nav.find_element(By.XPATH, '/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[3]/option[5]').click()
    matricular()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[8]/div[2]/div[2]/div[2]/input').click()
    alarme2=True
def procedimento_padrao_tp(a):
    global alarme2
    comeca_contagem()
    procedimento_padrao(a)
    comeca_contagem()
    escolher_botao_cpfcnpj_tp(a)
    nav.find_element(By.XPATH,'//*[@id="data_venda"]').click()
    #nav.find_element(By.XPATH,'//*[@id="data_venda"]').send_keys(str(arq['DATA REC'][a]))
    nav.find_element(By.XPATH, '//*[@id="CEP"]').click()
    nav.find_element(By.XPATH, '//*[@id="CEP"]').send_keys(Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE+str(arq.CEP[a]))
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[1]/option[2]').click()#interior
    #nav.find_element(By.XPATH,f'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[2]/option[{possibilidades.categorias_tp[arq.CATEGORIA[a].capitalize()]}]').click()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[3]/option[4]') .click()
    time.sleep(1)
    matricular()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[11]/div[2]/div[2]/div[2]/input').click()
    alarme2=True
def procedimento_padrao_t_plac (a):
    global alarme2
    alarme2 = False
    comeca_contagem()
    procedimento_padrao(a)
    escolher_botao_cpfcnpj_t_plac(a)
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/input[3]').send_keys(arq['CPF/CNPJ'][a])
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[1]/option[2]').click()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[2]/option[4]').click()
    matricular()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[7]/div[2]/div[2]/div[2]/input').click()
    alarme2=True
def procedimento_padrao_BX_GR(a):
    global alarme2
    alarme2 = False
    comeca_contagem()
    procedimento_padrao(a)
    escolher_botao_cpfcnpj_t_plac(a)
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/input[3]').send_keys(arq['CPF/CNPJ'][a])
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[1]/option[2]').click()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/select[2]/option[4]').click()
    matricular()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset/div[7]/div[2]/div[2]/div[2]/input').click()

    alarme2=True
#-----------------------------------------------bots-------------------------------------------------------------------------
def bot_segunda_via_crv():
    global alarme2
    alarme2=False
    comeca_contagem()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/ul/li[1]/input').click()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/div[1]/input').click()
    alarme2 = True
def bot_transferencia_de_juris(a):
    global alarme2
    alarme2=False
    comeca_contagem()
    nav.find_element(By.XPATH,f"/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/table[1]/tbody/tr/td/input[{str(possibilidades.servico_tj[arq.SERVICO[a]])}]").click()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/table[2]/tbody/tr/td[2]/div/img').click()
    alarme2 = True
def bot_tpm(a):
    global alarme2
    alarme2=False
    comeca_contagem()
    try:
        tipo=possibilidades.servico_tpm[arq.SERVICO[a]]
        nav.find_element(By.XPATH,f"/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/ul/li[{str(tipo)}]/input").click()
        nav.find_element(By.XPATH, '/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/div[1]/input[2]').click()
    except:
        nav.find_element(By.XPATH,'//*[@id="navSubmitF"]/input[1]').click()
        print("im here lor")
        selecionar_serv_extra_tpm(a)
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/div/input').click()

    alarme2 = True
def bot_tp(a):
    global alarme2
    alarme2=False
    comeca_contagem()
    tipo = possibilidades.servico_tp[arq.SERVICO[a]]
    nav.find_element(By.XPATH, f"/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/ul/li[{str(tipo)}]/input").click()
    nav.find_element(By.XPATH, '/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/div[1]/input[2]').click()
    alarme2=True
def bot_alt_carac(a):
    global alarme2
def bot_t_plac(a):
    global alarme2
    alarme2 = False
    comeca_contagem()
    palavras=separar_palavras(arq.SERVICO[a])
    for i in range(len(palavras)):
        try:
            #nav.find_element(By.XPATH,f'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset[2]/span[{possibilidades_PL_MERCOSUL[palavras[i]]}]/input').click
            nav.find_element(By.XPATH,f'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset[2]/span[{possibilidades.PL_MERCOSUL[palavras[i]]}]/input').click()
        except:
            print(f"falhou em{palavras[i]}")
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/div/input').click()
    alarme2=True
def bot_BX_GR(a):
    global alarme2
    alarme2 = False
    comeca_contagem()
    palavras = separar_palavras(arq.SERVICO[a])  # (arq.SERVICO[a])
    if 'CETIDAO' in palavras:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset[1]/span[2]/input').click()
    if 'BV' in palavras:
        nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/fieldset[2]/span/input').click()
    nav.find_element(By.XPATH,'/html/body/div[5]/div[4]/div/table/tbody/tr/td/form/div/input').click()
#---------------------------------------------------------------------------------------------------------------------
def remover_barras(word1):
    word2 = '/'
    for i in word2:
        word1 = word1.replace(i, '')
    return(str(word1))
def remover_traços(word1):
    word2 = '-'
    for i in word2:
        word1 = word1.replace(i, '')
    return(str(word1))
def remover_pontos(w):
    word2 = '.'
    for i in word2:
        w= w.replace(i, '')
    return (str(w))
def remover_ultimo_zero(w):
    if(w[len(w)-1]=='.0'):
        w=w[:-1]
    return(str(w))
def filtro_pro_bug(w):  #06/01/2022 -->20/22/0106    ---------d/m/y1y2-->y1/y2/md   {y2/y1/dm}
  w=remover_barras(w)
  w=remover_traços(w)
  dia=(w[0:2])
  mes=(w[2:4])
  ano1=(w[4:6])
  ano2=(w[6:8])
  return(f"{ano2}{ano1}{dia}{mes}")
def remover_0000000(w):
    word2 = '00:00:00'
    for i in word2:
        w = w.replace(i, '')
    return (str(w))

def separar_palavras(w):
  i=0
  num_of_w=0
  L_letra_anterior=0
  palavras=[]
  for letra in w:
    i+=1
    if letra=='/':
      palavras.append(remover_barras(w[L_letra_anterior:i]))
      num_of_w+=1
      L_letra_anterior=i
  palavras.append(remover_barras(w[L_letra_anterior:i]))
  return palavras
def separar_palavras_traco(w):
  i=0
  num_of_w=0
  L_letra_anterior=0
  palavras=[]
  for letra in w:
    i+=1
    if letra=='-':
      palavras.append(remover_barras(w[L_letra_anterior:i]))
      num_of_w+=1
      L_letra_anterior=i
  palavras.append(remover_barras(w[L_letra_anterior:i]))
  return palavras
#def bot_int_vend():

if __name__ == "__main__":
    time.sleep(1)