from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stellarburgers.nomoreparties.site/')

driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()

time.sleep(3)
driver.find_element(By.NAME, 'name').send_keys('Никита')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('110ree@gmail.com')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('012')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p').text == 'Некорректный пароль'

driver.quit()