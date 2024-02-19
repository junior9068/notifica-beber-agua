import logging, requests
import schedule, time

logging.basicConfig(filename='./log.log', format='%(asctime)s - %(levelname)s:%(message)s', level=logging.DEBUG)
copo = 0
litros = 0

def notificacao(mensagem):
    try:
        global copo
        global litros
        copo += 1
        litros = (copo * 200) / 1000
        texto = f"Tome água (200ml). Atingido: {litros} litros"
        requests.get(f"http://api.callmebot.com/whatsapp.php?phone=556183834741&text={texto}&apikey=4921157")
    except Exception as erro:
        logging.error(erro)
        exit(1)

schedule.every(1800).seconds.do(notificacao, mensagem="")

while True:
    schedule.run_pending()
    time.sleep(1)
    try:
        # Quando a quantidade de água ingerida chegar a 4 litros o programa é encerrado
        if litros >= 2:
            texto = "Você já atingiu a meta. Parabéns, Ruan!"
            requests.get(f"http://api.callmebot.com/whatsapp.php?phone=556183834741&text={texto}&apikey=4921157")
            exit(0)
    except Exception as erro:
        logging.error(erro)
        exit(1)