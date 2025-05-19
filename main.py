#pip install requests
import requests


while False:
    ask = input("Digite a moeda que você deseja converter: \nPossibilidades:\nReal = brl\nDolar = usd\nEuro = eur").lower()
    if ask == "brl" or ask == "usd" or ask == "eur":
        url = "https://www.floatrates.com/daily/"+ask+".json"
        retorno = requests.get(url)
        jsonConversão = retorno.json()
        ask2 = input("Digite a moeda que você deseja saber o valor: \nPossibilidades:\nReal = brl\nDolar = usd\nEuro = eur").lower()
        if ask2 == "brl" or ask2 == "usd" or ask2 == "eur":
            print(jsonConversão[ask2]['rate'])
        else:
            print("Insira uma das alternativas possiveis!!!")
    else:
        print("Insira uma das alternativas possiveis!!!")






def tamplate():  
    try:
        d = input("Digite um valor válido!")
        url = "https://www.floatrates.com/daily/"+d+".json"
        retorno = requests.get(url)
        jsonConversão  = retorno.json()

        print(jsonConversão['brl']['rate'])
    except:
        print("tente novamente")
    
tamplate()