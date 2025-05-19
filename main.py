#pip install requests
import requests



while False:
    ask = input("Digite a moeda que você deseja converter: \nPossibilidades:\nReal = brl\nDolar = usd\nEuro = eur").lower()
    #print(ask)
    if ask == "brl" or ask == "usd" or ask == "eur":
        def url(): 
                if ask == brl:
                    url = "https://www.floatrates.com/daily/brl.json"
                if ask == usd: 
                    url = "https://www.floatrates.com/daily/usd.json"
                if ask == eur: 
                    url = "https://www.floatrates.com/daily/eur.json"
        ask2 = input("Digite a moeda que você deseja saber o valor: \nPossibilidades:\nReal = brl\nDolar = usd\nEuro = eur")
    else:
        print("Insira uma das opções válidas!")


    
while True:
    ask = input("Digite a moeda que você deseja converter: \nPossibilidades:\nReal = brl\nDolar = usd\nEuro = eur").lower()
    url = "https://www.floatrates.com/daily/"+ask+".json"
    retorno = requests.get(url)
    jsonConversão = retorno.json()
    ask2 = input("Digite a moeda que você deseja saber o valor: \nPossibilidades:\nReal = brl\nDolar = usd\nEuro = eur")
    print(jsonConversão[ask2]['rate'])







def tamplate():  
    url = "https://www.floatrates.com/daily/usd.json"
    retorno = requests.get(url)
    jsonConversão  = retorno.json()

    print(jsonConversão['brl']['rate'])