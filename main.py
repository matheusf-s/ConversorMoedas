#pip install requests
import requests



try:
    ask = input("Digite a moeda que você deseja converter: " \
    "\n\033[31mPossibilidades:\nReal = brl\nDolar = usd\nEuro = eur\033[0m").lower()
    url = "https://www.floatrates.com/daily/"+ask+".json"
    retorno = requests.get(url)
    jsonConversão = retorno.json()


    try:
        quant = float(input("Quanto dessa moeda você deseja?"))



        try:
            ask2 = input("Digite a moeda que você deseja saber o valor: " \
            "\n\033[31mPossibilidades:\nReal = brl\nDolar = usd\nEuro = eur\033[0m").lower()
            print("A conversão de",quant,ask, "resulta em",round(jsonConversão[ask2]['rate'] * quant, 3), ask2, "\t\033[31m(Valor arrendondado!!)\033[0m")
        except:
            if ask == ask2:
                print("Não é possivel realizar a conversão de moedas iguais!")
            else:
                print("Insira uma das alternativas possiveis!!!")





    except:
        print("Digite um valor válido!!")



    
except:
    print("Digite uma nomenclatura válido!!")



