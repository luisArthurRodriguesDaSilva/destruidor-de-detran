<h1>destruidor de detran</h1>
 O <strong>destruidor de detran</strong> é uma automação feita por mim com o intuito de facilitar o agendamento de diversos tipos de documentos pois o site do detran contem uma quantidade um tanto excessiva de partes repetitivas que "devem" ser preenchidas manualmente
<br>
<br>

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