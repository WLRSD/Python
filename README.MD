<h1 align="center"> PYTHON </h1>
<img display="center" height="40" src="https://img.shields.io/badge/-python-05122A?style=flat&logo=python">
<br>
<h5>Repositório de estudos!</h5> 
<p align="justify">
Nesse repositório, desejo trazer meu avanço com a linguagem de programação, assim poderei revisitar quando esquecer certos
comandos, mas, também servirá de comprovação de minhas habilidades e de formas que encontrei na internet sobre o poder do Python
em diverentes áreas, desde <strong>DATA SCIENCE</strong> até <strong>WEB</strong>
</p>


- 📚 atualmente estou estudando pelo [DEV APRENDER](https://membros.devaprender.com/)
  ###### mas também estou seguindo o [RoadMap - Python](https://roadmap.sh/python) e também estou aprendendo com [Hashtag - Python](https://www.youtube.com/@HashtagProgramacao) e [Jetbrains](https://hyperskill.org/tracks)
<h3 align="center"> API NO PYTHON </h3>
<h5 align="center"> Conteúdo: Hashtag</h5> 
<br>
<h2> API - O QUE É? (Aplication Programing Interface): </h2>
 - é basicamente como um programa que acessa funcionalidade de outros sites.
 É muito utilizado para pegar/reaproveitar uma informação que já contém em outro site/programa
 <h4>EXEMPLO: Facebook</h4>
- A <strong>API</strong> do <strong>Facebook</strong> pode ser integrado como forma de login em seu <strong>site/programa</strong>. Assim você não precisa recriar a roda.
- O <strong>Facebook</strong> que irá filtrar o que você pode ou não fazer/ter acesso. É interessante você criar sua própria <strong>API</strong> para ter o conhecimento e conseguir demonstrar tal conhecimento para propostas de emprego. Mas, visando a facilidade no mundo cooporativo e reduzir tempo e dor de cabeça, utilizar <strong>API's</strong> já prontas e de grandes empresas <strong>(GOOGLE, YOUTUBE, AMAZON, FACEBOOK)</strong> facilita que não tenha que ser você a dar manutenção sempre.
<h3> FORMAS DE USAR UMA API: </h3>
 <strong>CONSUMINDO/RECEBENDO:</strong> Apenas conseguirá receber as informações, não tendo qualquer outro vínculo. Poderá apenas obter as informações da <strong>API</strong>; <br>
 <strong>ENVIANDO/REQUISITANDO:</strong> Podendo enviar solicitações de verificação à <strong>API</strong> e recebendo como resposta da solicitação uma solicitação.

# Estudo - Python 
### **Jetbrains**
Introdução ao Python:
- desenvolvido por Guido van Rossum em 1991
- Nome em homenagem a: Monty Python (grupo de comédia britânico)

## áreas de atuação
- Desenvolvimento Web:
Com auxílio dos frameworks **Django** e **Flask**, o _Python_ é capaz de construir sites dinamicamente.
##### Em meu projeto: [SiteFlask](https://github.com/WLRSD/SiteFlask) é possível ter uma noção de como é simples, de fácil compreensão a construção de sites em python. Porém, o **Flask** é visto como "básico", comparado ao **Django**.

- Ciência de dados:
Utilizando a biblioteca **Numpy**, **Pandas** e **TensorFlow** é possível utilizar o _Python_ para análises de dados e aprendizado de máquina!

- Scripting:
Acredito que seja a área em que o _Python_ começou ganhando mais destaque, sendo a área de **Automações de tarefas**. Para isso, é quase que indiscutível em comunidades e entre programadores, que o _Python_ é a linguagem certa para isso. Podendo automatizar desdes tarefas em ambiente local à automações online.

## Paradigma
O _Python_ é multiparadigma. Sendo **funcional**; **orientado a objetos**, **estruturado** e outros que aind não descobri.

## Sintaxe
A sintaxe (De acordo com o **Google**, a melhor forma de explicar é: _Sintaxe é o conjunto de regras que determina quais combinações de símbolos e palavras-chaves podem ser utilizadas em uma linguagem de programação_).

##### Exemplo de sintaxe em Python:
```Python
  age = input("How old are you? ")
  print("I know, that you're " + age + " years old")
```
##### Estrutura de indentação
No _Python_ não é necessário o uso do ';'. Porém, é necessário ter conhecimento sobre indentação, pois é algo que pode ocasionar em um erro genérico e sem muitas informações em seu código. O _Python_ trabalha com esse sistema, onde todo tipo de classe/função filho, tem que estar indentado na classe/função pai. Caso não esteja, pode ocasionar em erros. 

##### Comentário no Python:
Para comentar no _Python_ é só utilizar o '#' antes do comentário.

##### Case Sensitive:
No _Python_ é necessário ter cuidado com letras Maiúsculas e minúsculas, pois ele é _Case Sensitive_, o que implica dizer que uma letra maiúscula ou minúscula vai influenciar no código.

# DJANGO

### Para iniciar o projeto, foi necessário a instalação do **Anaconda Prompt**. Visto que foi necessário criar um **ambiente virtual** com uma versão do _python_ específica para trabalhar (no caso o **3.6**).

##### Caso queira saber o site para baixar o prompt do **Anaconda**: [Site Anaconda](https://www.anaconda.com/download), mas caso queira o passo-a-passo: [Vídeo - HASHTAG](https://www.youtube.com/watch?v=_eK0z5QbpKA).


#### Etapas para configurar o ambiente virtual para o Django:
- Entre no **Prompt Anaconda** e vá até o caminho de seus projetos (caso tenha), caso não tenha, vá até o caminho do **Desktop** mesmo e coloque seu projeto lá (será mais fácil para achar, caso não esteja muito acostumado com caminhos no prompt). Agora, conheça alguns comandos para facilitar a utilização do _CMD_:

```PowerShell
  dir
```
- Utilizado para listar todas as pastas que existem naquele diretório.
```PowerShell
  cd
```
- Utilizado para navegar entre diretórios/pastas.
```PowerShell
  mkdir [nomedapastacriada]
```
- Utilizado para criar um(a) diretório/pasta, signifca _make diretory_
```PowerShell
  cls
```
- Utilizado para limpar o terminal, voltando para a primeira linha do terminal.
```PowerShell
  cd..
```
- Utilizado para voltar para um diretório/pasta anterior.
```PowerShell
  conda create -n [nomedapastacriada] python=3.6
```
- Utilizado para criar o ambiente virtual do Django. E após isso, você deverá utilizar outro comando para **ativar** ele, que é o seguinte:
```PowerShell
  conda activate [nomedapastacriada]
```
E agora para finalizar, utilizando o **PIP**, instale o **DJANGO**.
```PowerShell
  pip install django
```
Quer saber todas bibliotecas instaladas pelo **pip**?
```PowerShell
  pip freeze
```
