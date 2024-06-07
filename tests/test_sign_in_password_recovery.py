from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stellarburgers.nomoreparties.site/login')

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a').click()

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset/div/div/input').send_keys('nikitakuleshov1991@yandex.ru')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

time.sleep(5)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/reset-password'

driver.quit()