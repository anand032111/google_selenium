from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://drive.google.com")
print(driver.title)
driver.find_element_by_xpath("//header//div[3]//div[1]//a[1]").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath("//input[@id='identifierId']").send_keys("testuser30071")
driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
driver.find_element_by_xpath("//input[@name='password']").send_keys("Test@3007")
driver.find_element_by_xpath("//div[@id='passwordNext']//div[2]").click()
driver.find_element_by_xpath("//body/div/div/div/div/div/div/div/div/div/button[1]").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//html//body//div//div//div//div//span//span//div[contains(text(),'Google Docs')]").click()
#act = ActionChains(driver)
#act.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER, Keys.ENTER).perform()
