from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from element import BasePageElement
from datetime import datetime

from locators import LoginPageLocators, BaseFaceBookPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def find(self, text):
        pass


class BaseFaceBookPage(BasePage):
    """Base class to initialize the base page that will be called from all pages"""

    def is_logged_in(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(BaseFaceBookPageLocators.LOGGED_IN_INDICATOR))




class HomePage(BaseFaceBookPage):


    def find(self, text):
        pass

    def show_profile(self):
        pass

    def show_about(self):
        pass


class LoginPage(BaseFaceBookPage):
    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_EMAIL)).send_keys(email)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_PASSWORD)).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_BTN)).submit()

    def is_displayed(self):
        try:
            li = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_BTN))
            em = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_EMAIL))
            pa = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_PASSWORD))
            return True
        except:
            return False


class ProfilePage(BaseFaceBookPage):
    def navigate_to_about(self):
        pass

    def birthday_found(self, date):
        self.navigate_to_about()
        date_str = date.strftime("%B % d, %Y")
        return self.find(date_str)

    def name_found(self, name):
        self.navigate_to_about()
        return self.find(name)
