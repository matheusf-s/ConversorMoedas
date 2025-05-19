#pip install requests
import requests



try:
    ask = input("ASK1\t\t\t""Digite a moeda que você deseja converter: \nPossibilidades:\nReal = brl\nDolar = usd\nEuro = eur").lower()
    url = "https://www.floatrates.com/daily/"+ask+".json"
    retorno = requests.get(url)
    jsonConversão = retorno.json()
except:
    print("Digite uma nomenclatura válido!!")



try:
    quant = float(input("Quanto dessa moeda você deseja?"))
except:
    print("Digite um valor válido!!")


    
try:
    ask2 = input("ASK2\t\t\t""Digite a moeda que você deseja saber o valor: \nPossibilidades:\nReal = brl\nDolar = usd\nEuro = eur").lower()
    print("A conversão de",quant,ask, "resulta em", ask2,round(jsonConversão[ask2]['rate'] * quant, 3), "\t(Valor arrendondado!!)")
except:
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
    
