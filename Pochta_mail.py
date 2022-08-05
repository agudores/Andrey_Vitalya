from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--incognito') #открыть хром в режиме инкогнито
browser = webdriver.Chrome(options = options)
link='https://account.mail.ru'
browser.get(link)

sleep(5) #ждём

#Вводим email
input1 = browser.find_element(By.CSS_SELECTOR, "#root > div > div.login-panel > div > div > div > div > form > div:nth-child(2) > div > div.login-row.username > div > div > div > div > div > div.base-0-2-64.first-0-2-70 > div > input")
input1.send_keys("example@mail.ru")

sleep(1) #ждём

#Нажать на кнопку далее
button = browser.find_element(By.CSS_SELECTOR, "#root > div > div.login-panel > div > div > div > div > form > div:nth-child(2) > div > div:nth-child(3) > div > div > div.submit-button-wrap > button > span")
button.click()

sleep(3) #ждём

#Вводим пароль
input2 = browser.find_element(By.CSS_SELECTOR, "#root > div > div.login-panel > div > div > div > div > form > div:nth-child(2) > div > div.login-row.password > div > div > div > div > div > input")
input2.send_keys("Пароль")

sleep(1) #ждём

#Нажать на кнопку далее
button = browser.find_element(By.CSS_SELECTOR, "#root > div > div.login-panel > div > div > div > div > form > div:nth-child(2) > div > div:nth-child(3) > div > div > div.submit-button-wrap > div > button > span")
button.click()
sleep(6) #ждём

try:
    check=browser.find_element(By.CSS_SELECTOR, ".compose-button__wrapper")
    if not check:
        print("не зашли")
    else:
        print("Хорошо")
finally:
    browser.quit()