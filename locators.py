from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    LOGIN_EMAIL = (By.ID, 'name="email"')
    LOGIN_PASSWORD = (By.ID, 'name="pass"')


