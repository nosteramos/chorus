import unittest
from selenium import webdriver
import page


class Tests(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
