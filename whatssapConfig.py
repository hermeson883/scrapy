import datetime
import time
from selenium.webdriver.common.by import By


def handleMessager(drive):
    # Escolhendo o grupo aonde se guarda mensagens
    group = drive.find_element(By.XPATH, "//span[@title='Repositório']")

    #CLicando nesse grupo
    group.click()

    #Dormindo até ele entrar na conversa
    time.sleep(1)

    #Pegando as mensagens
    messages = drive.find_elements(By.XPATH, "//div[@id='main']//div[@role='row']")

    #Pegando a ultima mensagem, onde está os contatos dos alunos
    messages = messages[-1]

    #Retornando o texto da mensagem
    return messages.text


def sendMessage(drive, person_infos, next_phone_number):
    #Pegando a hora atual
    day_month = datetime.datetime.now()

    #Filtrando apenas o dia e o mês
    day = day_month.day
    month = day_month.month

    #Se o mês for menor que o mês 10 insiro um nove na frete. Exemplo: mês 9 -> 09
    if month < 10:
        month = '0' + str(month)

    #Transformando ambos em strings
    day = str(day)

    #Procurando por esse Xpath
    find_number = drive.find_elements(By.XPATH,
                                      f"//div[@id='main']//div[contains(@data-pre-plain-text, '{day}/{month}')]")

    #Pegando a ultima mensagem mais uma vêz, onde se localiza os números dos alunos
    find_number = find_number[-1]

    #Pegando um atributo, onde fica os dados para localizar exatamente a ultima mensagem enviada onde se localiza os dados dos Alunos
    message_info = find_number.get_attribute('data-pre-plain-text')

    #Filtrando finalmente somente a mensagem especifica
    find_number.find_element(By.XPATH,
                             f"//div[@id='main']//div[contains(@data-pre-plain-text, '{message_info}')]/div/span[@dir='ltr']/span/a[{str(next_phone_number)}]").click()

    #Dormindo até ele clicar no elemento
    time.sleep(5)

    #Clicando no botão do WPP que vai levar para o contato da pessoa
    drive.find_element(By.XPATH, "//div[contains(@class, 'iWqod')]").click()

    #Dormindo até lá
    time.sleep(2)

    #Pegando a caixa de mensagens
    messageBox = drive.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]")

    #Deixando ela em foco
    messageBox.click()

    # Enviando o texto
    messageBox.send_keys(f"Olá {person_infos['name']},me chamo Hermeson message_info sou da Infinity School. Você marcou uma aula para dia{person_infos['date']}? Se sim, o que iremos ver?")

    #dormindo enquanto isso
    time.sleep(2)

    #Procurando pelo botão de enviar mensagem
    drive.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]/button").click()

    #Dormindo até lá
    time.sleep(2)

    #Voltando para o grupo 'Repositório'
    drive.find_element(By.XPATH, "//span[@title='Repositório']").click()
