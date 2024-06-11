from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, AuthPageLocators, PersonalAccountPageLocators

def test_sign_out(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys('nikitakuleshov1991@yandex.ru')
    driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys('01200120')
    driver.find_element(*AuthPageLocators.SUBMIT_BUTTON).click()
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BUTTON)).click()
    assert WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))
