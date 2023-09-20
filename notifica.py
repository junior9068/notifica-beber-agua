import logging
import subprocess
import schedule, time

qtd_ingerida_copos = int(input("Entre com a quantidade de copos que já ingeriu: "))
copo = qtd_ingerida_copos
litros = 0

def notificacao(mensagem):
    global copo
    global litros
    copo += 1
    litros = (copo * 200) / 1000
    subprocess.Popen(['notify-send', f"{mensagem} Atingido {litros} Litros"])
    logging.warning(f"Ingerido {litros} litros")

schedule.every(1800).seconds.do(notificacao, mensagem="Hora de tomar mais um copo de água.")

while True:
    schedule.run_pending()
    time.sleep(1)
