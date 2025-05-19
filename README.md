## Por que fiz este projeto

Desenvolvi este conversor de moedas para aprimorar minhas habilidades práticas em Python, especialmente no consumo de APIs e tratamento de dados externos. Escolhi trabalhar com conversão de moedas por ser um problema do mundo real que combina vários conceitos importantes de programação em um projeto compacto e útil. Além disso, queria criar algo que demonstrasse minha capacidade de desenvolver aplicações funcionais que interagem com serviços web.

## Como Usar

1. Execute o programa no terminal
2. Siga as instruções na tela:
- Digite o código da moeda de origem (brl, usd, eur)
- Informe o valor a ser convertido
- Escolha a moeda de destino
3. O resultado será exibido com o valor arredondado

Para sair do programa a qualquer momento, digite "q" quando solicitada a moeda de origem.

## Exemplo de Uso

Ao executar o programa, você verá instruções para:
1. Escolher a moeda de origem (ex: brl)
2. Informar o valor a ser convertido (ex: 100)
3. Escolher a moeda de destino (ex: usd)

O programa então mostrará o resultado da conversão com base nas taxas atuais.

## Tratamento de Erros

O programa inclui tratamento para:
- Tentativa de converter entre moedas iguais
- Entrada de valores não numéricos
- Códigos de moeda inválidos ou não suportados

## API Utilizada

Este projeto utiliza a API gratuita FloatRates (https://www.floatrates.com/json-feeds.html), que fornece taxas de câmbio atualizadas diariamente para diversas moedas.

## Conhecimentos Aplicados

Neste projeto, pude colocar em prática diversos conceitos importantes:
- Implementação de requisições HTTP em Python usando a biblioteca requests
- Aplicação de técnicas de tratamento de exceções em situações reais
- Manipulação prática de dados em formato JSON
- Desenvolvimento de interfaces de linha de comando com boa experiência de usuário