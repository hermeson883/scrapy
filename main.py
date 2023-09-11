import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from whatssapConfig import handleMessager, sendMessage
from infinity import handleInfinityDataToWpp

# Link para entrar no wpp
web = 'https://web.whatsapp.com/accept?code=Repositório'

# Caminho do driver de conexão do Chrome
path = 'D:\chrome_bin\chromedriver.exe'

# Instânciando o serviço
service = Service(path)

# Instânciando o drive para fazer 'consultas' no navegador
drive = Chrome(service=service)

handleInfinityDataToWpp(drive)

# Enviando para a função o handleMessager e passando o drive como parâmetro
messages = handleMessager(drive)

#tratando a mensagem
messages = messages.split('\n')
messages.pop() # Removendo a hora que a mensagem foi enviado

# Lista que irá guardar duplicatas dos números dos alunos
hasDuplicate = []

# Variável para pegar o número individual de cada aluno
next_phone = 1

# Loop por cada mensagem
for message in messages:
    # Tratando cada uma das mensagens individualmente
    text = message.split('-')
    print(text)

    # Pegando a informação de cada um dos alunos
    infos = {
        'hour' : text[0],
        'name' : text[1],
        'number' : text[2],
        'date' : text[-1]
    }

    # Checando se aquele número já foi processado
    if infos['number'] in hasDuplicate:
        next_phone += 1
        continue

    # Enviando para sendMessages
    sendMessage(drive, infos, next_phone)

    # Incrementando para ir para o próximo número
    next_phone += 1

    # Enviando para lista para nõa mandar novamente a mensagem para a pessoa
    hasDuplicate.append(infos['number'])
