import requests

while True:

    try:
        moeda_1 = input("Digite a moeda que você deseja converter: " \
        "\n\033[31mPossibilidades:\nReal = brl\nDolar = usd\nEuro = eur\033[0m" \
        "\n\033[32mCaso queira sair do código digite Q\033[0m").lower()
        if moeda_1 == "q":
            print("Programa encerrado, obrigado!")
            break
        url = "https://www.floatrates.com/daily/"+moeda_1+".json"
        retorno = requests.get(url)
        jsonConversão = retorno.json()

        try:
            quant = float(input("Quanto dessa moeda você deseja?"))

            try:
                moeda_2 = input("Digite a moeda que você deseja saber o valor: " \
                "\n\033[31mPossibilidades:\nReal = brl\nDolar = usd\nEuro = eur\033[0m").lower()
                print("A conversão de",quant,moeda_1, "resulta em",round(jsonConversão[moeda_2]['rate'] * quant, 3), moeda_2, "\t\033[31m(Valor arrendondado!!)\033[0m")
            except:
                if moeda_1 == moeda_2:
                    print("Não é possivel realizar a conversão de moedas iguais!")
                else:
                    print("Insira uma das alternativas possiveis!")

        except ValueError:
            print("Você digitou um valor invalido, por favor digite um valor correto!")

    except:
        print("Digite uma nomenclatura válido!")