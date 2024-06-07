from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from email_generation import email
from password_generating import password

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stellarburgers.nomoreparties.site/')

driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()

time.sleep(3)
driver.find_element(By.NAME, 'name').send_keys('Никита')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()


time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(email)
driver.find_element(By.NAME, 'Пароль').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
time.sleep(5)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

driver.quit()
