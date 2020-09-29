from POM.pages.DriveHomePage import GoogleDrivePage

class CreateNewFolder:
    def __init__(self, driver):
        self.click_on_create_button_xpath = None
        self.enter_folder_title_xpath = None
        self.createFolder_link_xpath = None

    def create_folder(self, title):
        dri =GoogleDrivePage()
        dri.driver.find_element_by_xpath(self.createFolder_link_xpath).click()
        dri.driver.find_element_by_xpath(self.enter_folder_title_xpath).send_keys(title)
        dri.driver.find_element_by_xpath(self.click_on_create_button_xpath).click()