#Aprendendo a mexer com API's no Python
#Utilizando API do AWESOME para cotação de Dolar, Real e BTC

import requests
import json 

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#A informação da API vem por padrão no formato JSON, agora é necessário formatar para o formato que o Python possa lê
cotacoes = cotacoes.json()
print(cotacoes)

#Agora vamos pegar a cotação específica de uma moeda, como por exemplo o Dolar:
#Dentro da variável é necessário passar o 'ID' da moeda, que no caso está vindo como String (padrão Json)
#Os valores que se encontram dentro do [] são os parâmetros, no caso, dentro do parâmetro do Dolar, quero que me traga
#o valor do bid (que é o valor da cotação atualmente)
cotacaoDolar = cotacoes['USDBRL']['bid']
print(cotacaoDolar)

#Com isso, aprendemos como funciona utilizar uma API no Python e como é possível formatar ele para o Python