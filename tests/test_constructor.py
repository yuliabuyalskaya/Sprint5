from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stellarburgers.nomoreparties.site/')

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]').click()
assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]').text == 'Начинки'

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]').click()
assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]').text == 'Соусы'

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]').click()
assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]').text == 'Булки'

driver.quit()

