import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, AuthPageLocators


def test_sign_in_personal_account(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys('nikitakuleshov1991@yandex.ru')
    driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys('01200120')
    driver.find_element(*AuthPageLocators.SUBMIT_BUTTON).click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    assert WebDriverWait(driver, 30).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))