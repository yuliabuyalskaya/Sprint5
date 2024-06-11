from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import AuthPageLocators, PasswordRecoveryLocators

def test_password_recovery(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(AuthPageLocators.FORGOT_PASSWORD_LINK)).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(PasswordRecoveryLocators.EMAIL_INPUT)).send_keys('nikitakuleshov1991@yandex.ru')
    driver.find_element(*PasswordRecoveryLocators.RESTORE_BUTTON).click()
    assert WebDriverWait(driver, 20).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/reset-password'))

