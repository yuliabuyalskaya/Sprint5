from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators

def test_buns_section(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(MainPageLocators.BUNS_BUTTON))
    driver.execute_script("arguments[0].click();", driver.find_element(*MainPageLocators.BUNS_BUTTON))
    assert driver.find_element(*MainPageLocators.BUNS_HEADER).text == 'Булки'

def test_sauces_section(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(MainPageLocators.SAUCES_BUTTON))
    driver.execute_script("arguments[0].click();", driver.find_element(*MainPageLocators.SAUCES_BUTTON))
    assert driver.find_element(*MainPageLocators.SAUSES_HEADER).text == 'Соусы'

def test_fillings_section(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_BUTTON))
    driver.execute_script("arguments[0].click();", driver.find_element(*MainPageLocators.FILLINGS_BUTTON))
    assert driver.find_element(*MainPageLocators.FILLINGS_HEADER).text == 'Начинки'
