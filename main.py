import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from whatssapConfig import handleMessager, sendMessages
from selenium.webdriver.common.by import By

web = 'https://web.whatsapp.com/accept?code=Repositório'

path = 'D:\chrome_bin\chromedriver.exe'
service = Service(path)

drive = Chrome(service=service)
drive.get(web)

time.sleep(20)

messages = handleMessager(drive)

messages = messages.split('\n')
messages.pop()
print(messages)

hasDuplicate = []

for message in messages:
    text = message.split('-')
    print(text)
    infos = {
        'hour' : text[0],
        'name' : text[1],
        'number' : text[2],
        'date' : text[-1]
    }

    # sendMessage(drive, infos)

    if infos['number'] in hasDuplicate:
        continue

    sendMessage(drive,infos)

    print(f'''
        Olá {infos['name']},me chamo Hermeson e sou da Infinity School. Você marcou uma aula para dia{infos['date']}? Se sim, o que iremos ver?
    ''')
    hasDuplicate.append(infos['number'])

