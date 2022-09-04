<h1>destruidor de detran</h1>
 O <strong>destruidor de detran</strong> é uma aplicação feita com o intuito de facilitar o agendamento de diversos tipos de documentos no site do detran pois ele contem um excesso de partes exautivamente repetitivas, o que permite uma automatização baseada em uma base de dados e um bot colocando-os no seu devido lugar, exigindo a participação humana apenas no final para o preenchimento do captcha e confirmação
<br></br>

<h2>serviços disponiveis</h2>
no momento estão disponiveis todos os serviços escritos nesse trecho de codigo,disponivel em <a href="https://github.com/luisArthurRodriguesDaSilva/destruidor-de-detran/blob/master/fs.py">fs.py</a>

```python
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
        
```

Todos os dados e informações devem estar em uma planilha seguindo esse modelo
<img src="imgs/WhatsApp Image 2022-09-04 at 19.18.41.jpeg">

as opções de serviço possiveis são relativas às presentes em <a href="https://www.detran.rj.gov.br/_documento.asp?cod=7620">agendamentos de veiculos </a> do site do detran
<img src="imgs/Captura de tela de 2022-04-21 22-42-38.png">

após o devido preenchimento da planilha assim com a instalação dos recursos nescessários o <strong>Destruidor de Detran</strong> deve se comportar dessa maneira

<img src="imgs/ezgif.com-gif-maker (2).gif">

<br></br>
# tecnologias e bibliotecas usadas
<ul>
<li><h2><a href="https://selenium-python.readthedocs.io/">Selenium</a></h2></li>
<li><a href="https://chromedriver.chromium.org/downloads" ><h2>Chromedriver</h2></a></li>
<li><a href="https://pyautogui.readthedocs.io/en/latest/" ><h2>Pyautogui</h2></a></li>
<li><a href="https://docs.python.org/3/library/threading.html" ><h2>Treads (para melhoria do desempenho)</h2></a></li>
</ul>
