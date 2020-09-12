from selenium import webdriver
import unittest
import HtmlTestRunner


class GoogleDocs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # executable_path='/Users/priyamvadaanand/PycharmProjects/google_selenium/driver/chromedriver'
        # cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_Login_To_Google_Doc(self):
        self.driver.get("https://docs.google.com")
        self.driver.find_element_by_xpath("//input[@id='identifierId']").send_keys("testuser30071")
        self.driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
        self.driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/screenshots/img1.png")
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("Test@3007")
        self.driver.find_element_by_xpath("//div[@id='passwordNext']//div[2]").click()
        self.driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/screenshots/img2.png")
        self.driver.find_element_by_xpath(
            "//body/div/div/div/div/div/div/div/div/header[@id='gb']/div[2]/div//*[local-name()='svg']").click()
        self.driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/screenshots/img3.png")
        self.driver.find_element_by_xpath("//div[contains(text(),'Docs')]").click()
        self.driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/screenshots/img4.png")
        self.driver.find_element_by_css_selector(
            "body.docs-gm.docs-homescreen-snackbar-enabled.docs-homescreen-material-bar-enabled.docs-homescreen"
            "-templates-enabled:nth-child(2) div.docs-homescreen-container.docs-homescreen-docs:nth-child(3) "
            "div.docs-homescreen-homescreenmain "
            "div.docs-homescreen-fcc-inlinecontainer.docs-homescreen-fcc-inlinecontainer-docked:nth-child(1) "
            "div.docs-homescreen-fcc-flex.docs-homescreen-fcc-flex-contracted "
            "div.docs-homescreen-fcc-flex-content-wrapper div.docs-homescreen-fcc-content "
            "div.docs-hs-tmp-sch.docs-hs-tmp-sch-swe.docs-hs-tmp-templatecontentholder div.docs-hs-tmp-sch-content "
            "div.docs-hs-tmp-templatecontentholder-inline "
            "div.docs-hs-tmp-sch.docs-hs-tmp-sch-content.docs-hs-tmp-sch-ns.docs-hs-tmp-alwaysvisiblecontentholder "
            "div.docs-hs-tmp-widthwrapper div.docs-homescreen-itemholder-content.docs-homescreen-templates-gallery "
            "div.docs-homescreen-grid-container.docs-homescreen-grid-container-horizontal.docs-hs-tmp-sc-showcase:nth"
            "-child(1) div.docs-homescreen-item-section "
            "div.docs-homescreen-templates-templateview.docs-homescreen-templates-templateview-showcase:nth-child(1) "
            "div.docs-homescreen-templates-templateview-preview.docs-homescreen-templates-templateview-preview"
            "-showcase > img:nth-child(1)").click()
        self.driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/screenshots/img5.png")
        self.driver.title
        self.driver.find_element_by_class_name("kix-page-column").click()
        self.driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/screenshots/img6.png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="/Users/priyamvadaanand/PycharmProjects/google_selenium/reports"))
