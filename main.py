import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Configurações de monitoramento
limite_cpu_percent = 90.0
limite_memoria_percent = 90.0
limite_espaco_disco_percent = 90.0

# Configurações de email
remetente_email = 'seu_email@gmail.com'
senha_email = 'sua_senha'
destinatario_email = 'destinatario@email.com'

def enviar_email(subject, message):
    msg = MIMEMultipart()
    msg['From'] = remetente_email
    msg['To'] = destinatario_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente_email, senha_email)
        server.sendmail(remetente_email, destinatario_email, msg.as_string())
        server.quit()
    except Exception as e:
        logging.error(f'Erro ao enviar o email: {e}')

def monitorar_recursos():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        memoria_percent = psutil.virtual_memory().percent
        espaco_disco_percent = psutil.disk_usage('/').percent

        if cpu_percent >= limite_cpu_percent:
            enviar_email('Alerta de Uso de CPU', f'Uso de CPU atingiu {cpu_percent}%')

        if memoria_percent >= limite_memoria_percent:
            enviar_email('Alerta de Uso de Memória', f'Uso de memória atingiu {memoria_percent}%')

        if espaco_disco_percent >= limite_espaco_disco_percent:
            enviar_email('Alerta de Espaço em Disco', f'Espaço em disco atingiu {espaco_disco_percent}%')

        time.sleep(1)

if __name__ == "__main__":
    monitorar_recursos()
