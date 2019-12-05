from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    LOGIN_EMAIL = (By.NAME, 'email')
    LOGIN_PASSWORD = (By.NAME, 'pass')
    LOGIN_BTN = (By.CSS_SELECTOR, '[data-testid="royal_login_button"]')


class MainPageLocators(object):
    PROFILE_ICON = (By.CSS_SELECTOR, 'a[href="https://www.facebook.com/amos.mastbaum"')


class BaseFaceBookPageLocators(object):
    LOGGED_IN_INDICATOR = (By.XPATH, '//textarea[@title="What\'s on your mind, Amos?"]')
