from selenium.webdriver.common.by import By


class AuthPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="Пароль"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button.button_button__33qZ0')
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, 'Восстановить пароль')
    RESTORE_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'button.button_button__33qZ0')


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'a[href="/account"] p')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.button_button__33qZ0')
    LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, 'ul li a[href="/"] p')
    BUNS_BUTTON = (By.CSS_SELECTOR, 'div.tab_tab__1SPyG:nth-child(1)')
    SAUCES_BUTTON = (By.CSS_SELECTOR, 'div.tab_tab__1SPyG:nth-child(2)')
    FILLINGS_BUTTON = (By.CSS_SELECTOR, 'div.tab_tab__1SPyG:nth-child(3)')
    BUNS_HEADER = (By. CSS_SELECTOR,'h2.text_type_main-medium:nth-child(1)')
    SAUSES_HEADER = (By. CSS_SELECTOR,'h2.text:nth-child(3)')
    FILLINGS_HEADER = (By. CSS_SELECTOR,'h2.text:nth-child(5)')

class RegistrationPageLocators:
    NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button.button_button_type_primary__1O7Bx')
    LOGIN_LINK = (By.LINK_TEXT, 'Войти')
    INVALID_PASSWORD_WARNING = (By.CSS_SELECTOR, '.input__error')


class PersonalAccountPageLocators:
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '.Account_button__14Yp3')


class PasswordRecoveryLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    RESTORE_BUTTON = (By.CSS_SELECTOR, 'button.button_button__33qZ0')



