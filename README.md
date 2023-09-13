# Calculadora de CR - UFABC com Python

Uma calculadora feita 100% em Python que calcula o CR (Coeficiente de Rendimento) de um aluno da UFABC a partir das disciplinas e notas fornecidas. 

##

Este projeto foi criado após terminar os 3 módulos do curso de Python do canal [Curso em Vídeo](https://www.youtube.com/@CursoemVideo) no YouTube como forma de me desafiar e me ajudar no dia a dia, tendo em mente que entender como está a situação do seu CR é vital para auxiliá-lo a conseguir se matricular em disciplinas.

Assim, decidi botar a mão na massa e criar este projeto.

# Funcionamento
Usando as bibliotecas `os`, `time` e `json`, o projeto mostra ao usuário um menu onde ele pode escolher a opção desejada:

![MENU](https://raw.githubusercontent.com/AlysonCantalice/CalculadoraCR-UFABC/main/images/demo1.png)

Navegando nesta tela, temos as seguintes opções:

## 0. Mostrar lista do CR

![MostrarCR](https://raw.githubusercontent.com/AlysonCantalice/CalculadoraCR-UFABC/main/images/demo3.png)

Mostra as matérias cadastradas até então, gerando um código único para cada uma delas e o total de créditos cursados até então, mostrando em seguida o CR calculado com base nestas matérias.

## 1. Adicionar Matéria

![AddMat](https://raw.githubusercontent.com/AlysonCantalice/CalculadoraCR-UFABC/main/images/demo2.png)

Pede para que seja informado o nome, créditos e conceito obtido na disciplina, adicionando esta matéria ao cálculo de CR, fornecendo a opção de continuar adicionando mais disciplinas conforme julge necessário.

## 2. Editar Matéria

![EditMat](https://raw.githubusercontent.com/AlysonCantalice/CalculadoraCR-UFABC/main/images/demo4.png)

Caso necessário, o programa também disponibiliza uma forma de editar ou remover uma matéria, podendo assim atualizar qualquer campo de determinada matéria que precise, identificando a matéria atravéz de seu código.

## 3. Carregar e 4. Salvar

Estas opções dão ao usuário a opção de salvar e carregar as matérias atualmente cadastradas através de um arquivo .json, criando-o caso seja a primeira vez que o usuário esteja salvando alguma matéria.

# Requisitos

Como qualquer outro programa criado em Python, é necessário ter o mesmo instalado em sua máquina para garantir com que este programa funcione. Para isso, basta acessar o site oficial [Python](https://www.python.org/downloads/) e instalar.

##

Criado por @AlysonCantalice