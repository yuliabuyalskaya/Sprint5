
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.email_generation import email
from helpers.password_generating import password
from locators.locators import RegistrationPageLocators
from selenium.webdriver.common.by import By

def test_registration(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Nikita')
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    assert WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))
