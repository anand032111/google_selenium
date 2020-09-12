from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from PageObjectModel.Pages.login import LoginPage
from PageObjectModel.Pages.googledoc import GoogleDocsPage


class GoogleDocs(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # executable_path='/Users/priyamvadaanand/PycharmProjects/google_selenium/driver/chromedriver'
        # cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_Login_To_Google_Doc(self):
        driver = self.driver
        driver.get("https://docs.google.com")

        login = LoginPage(driver)
        login.enter_username("testuser30071")
        login.click_on_next_button()
        login.enter_password("Test@3007")
        login.click_on_pwd_next_button()

        doc = GoogleDocsPage(driver)
        doc.click_navigation_icon()
        doc.click_doc_icon()
        doc.click_plus_icon()
        doc.click_on_doc_page()

        driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="/Users/priyamvadaanand/PycharmProjects/google_selenium/PageObjectModel/reports"))
