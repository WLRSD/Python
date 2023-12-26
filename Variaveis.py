#Primeiro Desafio - DEV APRENDER
#Retorne o tipo de dado de cada variável:
variavel_1 = 25.87
variavel_2 = True
variavel_3 = 'Bom dia!'
variavel_4 = 15

#Necessário formatar o tipo do dado em texto para conseguir concatenar com a mensagem
mensagem1 = "O tipo do dado e: " + str(type(variavel_1))
mensagem2 = "O tipo do dado e: " + str(type(variavel_2))
mensagem3 = "O tipo do dado e: " + str(type(variavel_3))
mensagem4 = "O tipo do dado e: " + str(type(variavel_4))

print(mensagem1)
print(mensagem2)
print(mensagem3)
print(mensagem4)

#Como criar uma váriavel: O valor é alocado na variável criada (10 está alocado em velocidadeInternet)
velocidadeInternet = 10 

#Quais tipos de dados podemos trabalhar:
#Booleanos
esta_aberta = True
#Números
velocidadeInternet = 10
#Strings - pode ser feito com "" ou ''
slogan = 'feito é melhor que perfeito'

#Como alocar várias variáveis: unpackings
a,b,c,d = 1,False,'Sim',4.5

#Como mostrar no console: 
#comando para duplicar a linha: alt + shift + seta para baixo
print(a)
print(b)
print(c)
print(d)
