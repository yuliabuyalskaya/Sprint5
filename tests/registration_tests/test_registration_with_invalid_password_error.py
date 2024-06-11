from helpers.email_generation import email
from locators.locators import RegistrationPageLocators

def test_registration_with_invalid_password_error(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Никита')
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('123')
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    assert driver.find_element(*RegistrationPageLocators.INVALID_PASSWORD_WARNING).text == 'Некорректный пароль'