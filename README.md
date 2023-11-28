# Script Python que gera notificação no ubuntu

# Preparando o ambiente (ubuntu):

1 - Instale o venv para o projeto ser executado em um ambiente isolado:

`python3 -m pip install --user virtualenv` 

2 - Instale as dependências do projeto:

`pip install requests`

3 - Crie o ambiente isolado com o venv:

 `python3 -m venv venv`

4 - Habilite o ambiente islolado:

`source venv/bin/activate`

5 - Instale a biblioteca schedule:

`pip install schedule`

## Executando o script

Para executar o script e ser notificado de 30 em 30 minutos, execute o comando:

`python3 notifica.py`


# Preparando o ambiente (WhatsApp)

Para enviar mensagem para o WhatsApp você precisa utilizar o serviço gratuito chamado CallMeBot (https://www.callmebot.com).

Como funciona: 

Você solicita uma chave de acesso (chave de acesso a API) e com essa chave você consegue fazer uma chamada via API para o bot te enviar uma 
mensagem que vc pode programar.

Siga os passos para conseguir a chave de acesso:

1 - Adicione o contato do CallMeBot na sua lista de contatos. Você encontra o número aqui nesta url: https://www.callmebot.com/blog/free-api-whatsapp-messages/

2 - Colocar sua chave da API e o seu número de telefone com o 55 e o DDD na URL que está no script `notifica_zap.py`. EX:

```
http://api.callmebot.com/whatsapp.php?phone=5561999999999&text={texto}&apikey=00000

```

3 - Se quiser, configure o crontab para executar o script na hora que desejar. Exemplo para o Cron utilizando o crontab do ubuntu:

```
# m h  dom mon dow   command
0 8 * * * /usr/bin/python3 /home/edilson/projetos/notifica-beber-agua/notifica_zap.py
```

No exemplo co cron acima, o script será executado todos os dias às 08:00 horas da manhã.

