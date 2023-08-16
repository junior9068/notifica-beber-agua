# Script Python que gera notificação no ubuntu

## Preparando o ambiente (ubuntu):

1 - Instale o venv para o projeto ser executado em um ambiente isolado:

`python3 -m pip install --user virtualenv` 

2 - Crie o ambiente isolado com o venv:

 `python3 -m venv venv`

3 - Habilite o ambiente islolado:

`source venv/bin/activate`

4 - Instale a biblioteca schedule:

`pip install schedule`

## Executando o script

Para executar o script e ser notificado de 30 em 30 minutos, execute o comando:

`python3 notifica.py`
