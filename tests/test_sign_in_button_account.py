from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stellarburgers.nomoreparties.site/register')

driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()
current_url = driver.current_url
assert current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('nikitakuleshov1991@yandex.ru')
driver.find_element(By.NAME, 'Пароль').send_keys('01200120')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
time.sleep(5)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

driver.quit()