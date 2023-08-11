# Script Python que gera notificação no ubuntu

## Preparando o ambiente:

1 - Instale o venv para o projeto ser executado em um ambiente isolado:

`pip install venv` 

2 - Crie o ambiente isolado com o venv:

 `python3 -m venv venv`

3 - Habilite o ambiente islolado:

`source venv/bin/activate`

4 - Instale a biblioteca schedule:

`pip install schedule`

## Executando o script

Para executar o script e ser notificado de 30 em 30 minuto, execute o comando:

`python3 notifica.py`
