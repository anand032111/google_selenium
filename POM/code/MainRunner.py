import time

from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POM.pages.DriveLoginPage import LoginPage
from POM.pages.DriveHomePage import GoogleDrivePage
from POM.pages.DocHomePage import DocHomePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from POM.pages.CreateFolder import CreateNewFolder

class GoogleDrive(unittest.TestCase):
    driver = None

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    # def test_Login_To_Google_Sheet(self):
    #     driver = self.driver
    #     driver.get("https://drive.google.com")
    #     print(driver.title)
    #     driver.find_element_by_xpath("//header//div[3]//div[1]//a[1]").click()
    #     driver.switch_to.window(driver.window_handles[1])
    #     login = LoginPage(driver)
    #     login.enter_username("testuser30071")
    #     login.click_on_next_button()
    #     login.enter_password("Test@3007")
    #     login.click_on_pwd_next_button()
    #     drive = GoogleDrivePage(driver)
    #     drive.click_new_button()
    #     drive.click_google_sheet()
    #     print("Welcome to Google Sheet")
    #     driver.switch_to.window(driver.window_handles[2])
    #     print(driver.title)
    #     driver.find_element_by_css_selector("input[class='docs-title-input']").click()
    #     driver.implicitly_wait(3)
    #     act = ActionChains(driver)
    #     act.send_keys(Keys.BACKSPACE).perform()
    #     driver.get_screenshot_as_file(
    #         "/Users/priyamvadaanand/PycharmProjects/google_selenium/POM/screenshots/Sheettitlecleared.png")
    #     driver.find_element_by_xpath("//*[@id='docs-title-widget']/input").send_keys("Automation Sheet Experiment")
    #     driver.get_screenshot_as_file(
    #         "/Users/priyamvadaanand/PycharmProjects/google_selenium/POM/screenshots/Sheettitleupdated.png")
    #     time.sleep(3)

    # def test_Login_to_Google_Doc(doc):
    #     driver = doc.driver
    #     driver.get("https://drive.google.com")
    #     print(driver.title)
    #     driver.find_element_by_xpath("//header//div[3]//div[1]//a[1]").click()
    #     driver.switch_to.window(driver.window_handles[1])
    #     login = LoginPage(driver)
    #     login.enter_username("testuser30071")
    #     login.click_on_next_button()
    #     login.enter_password("Test@3007")
    #     login.click_on_pwd_next_button()
    #     drive = GoogleDrivePage(driver)
    #     drive.click_new_button()
    #     drive.click_google_doc()
    #     print("welcome to Google Doc")
    #     driver.switch_to.window(driver.window_handles[2])
    #     print(driver.title)
    #     googledoc = DocHomePage(driver)
    #     googledoc.click_on_title()
    #     driver.implicitly_wait(3)
    #     act = ActionChains(driver)
    #     act.send_keys(Keys.BACKSPACE).perform()
    #     driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/google_selenium/POM/screenshots/DocTiltleCleared.png")
    #     googledoc.document_title("Automation Doc Experimet")
    #     #driver.find_element_by_xpath("//*[@id='docs-title-widget']/input").send_keys("Automation Doc Experiment")
    #     driver.get_screenshot_as_file(
    #         "/Users/priyamvadaanand/PycharmProjects/google_selenium/POM/screenshots/DocTitleUpdated.png")

    # def test_Login_to_Google_slides(sld):
    #     driver = sld.driver
    #     driver.get("https://drive.google.com")
    #     print(driver.title)
    #     driver.find_element_by_xpath("//header//div[3]//div[1]//a[1]").click()
    #     driver.switch_to.window(driver.window_handles[1])
    #     login = LoginPage(driver)
    #     login.enter_username("testuser30071")
    #     login.click_on_next_button()
    #     login.enter_password("Test@3007")
    #     login.click_on_pwd_next_button()
    #     drive = GoogleDrivePage(driver)
    #     drive.click_new_button()
    #     drive.click_google_slide()
    #     print("welcome to Google Slide")
    #     driver.switch_to.window(driver.window_handles[2])
    #     print(driver.title)
    #     driver.find_element_by_css_selector("input[class='docs-title-input']").click()
    #     driver.implicitly_wait(3)
    #     act = ActionChains(driver)
    #     act.send_keys(Keys.BACKSPACE).perform()
    #     driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/google_selenium/POM/screenshots/SlideTiltleCleared.png")
    #     driver.find_element_by_xpath("//*[@id='docs-title-widget']/input").send_keys("Automation Slide Experiment")
    #     driver.get_screenshot_as_file(
    #         "/Users/priyamvadaanand/PycharmProjects/google_selenium/POM/screenshots/SlideTitleUpdated.png")

    def test_Login_to_Google_createfolder(fld):
        driver = fld.driver
        driver.get("https://drive.google.com")
        print(driver.title)
        driver.find_element_by_xpath("//header//div[3]//div[1]//a[1]").click()
        driver.switch_to.window(driver.window_handles[1])
        login = LoginPage(driver)
        login.enter_username("testuser30071")
        login.click_on_next_button()
        login.enter_password("Test@3007")
        login.click_on_pwd_next_button()
        drive = GoogleDrivePage(driver)
        drive.click_new_button()
        drive.create_folder("testcase6")
        time.sleep(2)
        drive.click_new_button()
        drive.create_folder("testcase7")

        time.sleep(5)



    @classmethod
    # def tearDownClass(cls):
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="/Users/priyamvadaanand/PycharmProjects/google_selenium/POM/reports"))
