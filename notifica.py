import subprocess
import schedule, time

qtd_ingerida_copos = int(input("Entre com a quantidade de copos que já ingeriu: "))
copo = qtd_ingerida_copos
def notificacao(mensagem):
    global copo
    copo += 1
    litros = (copo * 200) / 1000
    subprocess.Popen(['notify-send', f"{mensagem} Atingido {litros} Litros"])


schedule.every(1800).seconds.do(notificacao, mensagem=f"Hora de tomar mais um copo de água.")

while True:
    schedule.run_pending()
    time.sleep(1)