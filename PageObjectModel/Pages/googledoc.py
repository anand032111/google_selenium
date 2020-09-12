class GoogleDocsPage:

    def __init__(self,driver):

        self.driver = driver
        self.navigation_icon_xpath="//body/div/div/div/div/div/div/div/div/header[@id='gb']/div[2]/div//*[local-name()='svg']"
        self.icon_docs_xpath ="//div[contains(text(),'Docs')]"
        self.click_on_page_class_name="kix-page-column"
        #self.click_on_plus_icon_css_selector="holder-inlinebody.docs-gm.docs-homescreen-snackbar-enabled.docs-homescreen-material-bar-enabled.docs-homescreen-templates-enabled:nth-child(2) div.docs-homescreen-container.docs-homescreen-docs:nth-child(3) div.docs-homescreen-homescreenmain div.docs-homescreen-fcc-inlinecontainer.docs-homescreen-fcc-inlinecontainer-docked:nth-child(1) div.docs-homescreen-fcc-flex.docs-homescreen-fcc-flex-contracted div.docs-homescreen-fcc-flex-content-wrapper div.docs-homescreen-fcc-content div.docs-hs-tmp-sch.docs-hs-tmp-sch-swe.docs-hs-tmp-templatecontentholder div.docs-hs-tmp-sch-content div.docs-hs-tmp-templatecontent div.docs-hs-tmp-sch.docs-hs-tmp-sch-content.docs-hs-tmp-sch-ns.docs-hs-tmp-alwaysvisiblecontentholder div.docs-hs-tmp-widthwrapper div.docs-homescreen-itemholder-content.docs-homescreen-templates-gallery div.docs-homescreen-grid-container.docs-homescreen-grid-container-horizontal.docs-hs-tmp-sc-showcase:nth-child(1) div.docs-homescreen-item-section div.docs-homescreen-templates-templateview.docs-homescreen-templates-templateview-showcase:nth-child(1) div.docs-homescreen-templates-templateview-preview.docs-homescreen-templates-templateview-preview-showcase > img:nth-child(1)"
        self.click_on_Blank_page_xpath="//body//div//div//div//div//div//div//div//div//div//div//div//div//div[1]//div[1]//div[1]//img[1]"


    def click_navigation_icon(self):
        self.driver.find_element_by_xpath(self.navigation_icon_xpath).click()

    def click_doc_icon(self):
        self.driver.find_element_by_xpath(self.icon_docs_xpath).click()

    def click_plus_icon(self):
        self.driver.find_element_by_xpath(self.click_on_Blank_page_xpath).click()

    def click_on_doc_page(self):
        self.driver.find_element_by_class_name(self.click_on_page_class_name).click()