import time
from selenium.webdriver.common.by import By
from whatssapConfig import sendToMessageBox

def handleInfinityDataToWpp(drive):
    infinity = 'https://www.infinityschool.app/area_restrita'

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

    sendToMessageBox(drive, contact)