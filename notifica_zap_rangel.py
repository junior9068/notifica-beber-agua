import logging, requests
import schedule, time

copo = 0
litros = 0

def notificacao(mensagem):
    global copo
    global litros
    copo += 1
    litros = (copo * 200) / 1000
    # subprocess.Popen(['notify-send', f"{mensagem} Atingido {litros} Litros"])
    texto = f"Tome água (200ml). Atingido: {litros} litros"
    requests.get(f"http://api.callmebot.com/whatsapp.php?phone=557799519703&text={texto}&apikey=3972964")


schedule.every(1800).seconds.do(notificacao, mensagem="")

while True:
    schedule.run_pending()
    time.sleep(1)
    # Quando a quantidade de água ingerida chegar a 4 litros o programa é encerrado
    if litros >= 3:
        texto = "Você já atingiu a meta. Parabéns!"
        requests.get(f"http://api.callmebot.com/whatsapp.php?phone=557799519703&text={texto}&apikey=3972964")
        exit(0)