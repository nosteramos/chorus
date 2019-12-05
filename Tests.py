import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import page


class Tests(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        options = Options()
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome("chromedriver.exe", options=options)
        self.driver.get("https://www.facebook.com")
        login_page = page.LoginPage(self.driver)
        if login_page.is_displayed():
            login_page.login("nosteramos@gmail.com", "!noamassaf1")
        home_page = page.HomePage(self.driver)
        assert home_page.is_logged_in()

    def test_facebook(self):
        pass

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
