import requests

def via_cep(cep):
    bairro = ''
    info = requests.get("https://viacep.com.br/ws/" + str(cep) + "/json/")
   # print(info.text)    #Para imprimir todas as informações do CEP

    return(info.json()['bairro'])