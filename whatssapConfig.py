import datetime
import time
from selenium.webdriver.common.by import By



def handleMessager(drive):
    group = drive.find_element(By.XPATH, "//span[@title='Repositório']")

    group.click()

    time.sleep(2)

    messages = drive.find_elements(By.XPATH, "//div[@id='main']//div[@role='row']")

    messages = messages[-1]

    return messages.text

# //div[@id='main']//div[@role='row']//span[@dir='ltr']

# //div[@id='main']//div[@role='row']

def sendMessages(drive, info):
    links = drive.find_elements(By.XPATH, "//div[@id='main']//div[@role='row']")
    links = links[-1]
    links = links.find_elements(By.XPATH, "//div[contains(@data-pre-plain-text, '05')]")
    # Isso dá certo


# def sendMessage(drive, user_info):
#     links = drive.find_elements(By.XPATH, "//div[@id='main']//div[@data-pre-plain-text]")
#     links = links[-1]
#     print(links.text, user_info)

# Pegar elementos
# //div[@id='main']//div[@role='row']//span[@dir='ltr']//span//a

