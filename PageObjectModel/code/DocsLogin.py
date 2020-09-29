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
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_Login_To_Google_Doc(self):
        driver = self.driver
        driver.get("https://docs.google.com")
        login = LoginPage(driver)
        login.enter_username("testuser30071")
        driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/google_selenium/PageObjectModel/screenshots/image1.png")
        login.click_on_next_button()
        login.enter_password("Test@3007")
        driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/google_selenium/PageObjectModel/screenshots/image2.png")
        login.click_on_pwd_next_button()
        doc = GoogleDocsPage(driver)
        doc.click_navigation_icon()
        driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/PageObjectModel/screenshots/image3.png")
        doc.click_doc_icon()
        driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/PageObjectModel/screenshots/image4.png")
        doc.click_plus_icon()
        driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/PageObjectModel/screenshots/image5.png")
        doc.click_on_doc_page()
        driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/PageObjectModel/screenshots/image6.png")
        driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="/Users/priyamvadaanand/PycharmProjects/google_selenium/PageObjectModel/reports"))


