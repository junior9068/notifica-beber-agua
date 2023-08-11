import subprocess
import schedule, time

copo = 0
def notificacao(mensagem):
    global copo
    copo += 1
    litros = (copo * 200) / 1000
    subprocess.Popen(['notify-send', f"{mensagem} Atingido {litros} Litros"])


schedule.every(1800).seconds.do(notificacao, mensagem=f"Hora de tomar mais um copo de água.")

while True:
    schedule.run_pending()
    time.sleep(1)