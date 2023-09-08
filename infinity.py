import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

infinity = 'https://www.infinityschool.app/area_restrita'
path = 'D:\chrome_bin\chromedriver.exe'
service = Service(path)

drive = Chrome(service=service)
drive.get(infinity)

time.sleep(5)

input_field = drive.find_element(By.XPATH, '//div/form/div/input')

input_field.click()
input_field.send_keys('dev04')

drive.find_element(By.XPATH, '//div/form/center/button').click()

time.sleep(5)

repos = drive.find_elements(By.XPATH, "(//div/center/h2/font[contains(text(), 'Particular')] | //div/center/h2/font[contains(text(), 'Online')] | //div/center/h2/font[contains(text(), 'presencial')])")


contact = []

for repo in repos:
    contact.append(repo.text)

drive.get('https://web.whatsapp.com/')

time.sleep(20)

drive.find_element(By.XPATH, "//span[@title='Repositório']").click()

time.sleep(5)

messageBox = drive.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]")

# Deixando ela em foco
messageBox.click()
print(contact)
# Enviando o texto
messageBox.send_keys(contact)

# dormindo enquanto isso
time.sleep(2)

# Procurando pelo botão de enviar mensagem
drive.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]/button").click()

# Dormindo até lá
time.sleep(2)

# Voltando para o grupo 'Repositório'
drive.find_element(By.XPATH, "//span[@title='Repositório']").click()

time.sleep(5)