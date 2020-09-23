from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://drive.google.com")
driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/google_selenium/images/img1.png")
print(driver.title)
driver.find_element_by_xpath("//header//div[3]//div[1]//a[1]").click()
driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/google_selenium/images/img2.png")
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath("//input[@id='identifierId']").send_keys("testuser30071")
driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/google_selenium/images/img3.png")
driver.find_element_by_xpath("//input[@name='password']").send_keys("Test@3007")
driver.find_element_by_xpath("//div[@id='passwordNext']//div[2]").click()
driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/google_selenium/images/img4.png")
driver.find_element_by_xpath("//body/div/div/div/div/div/div/div/div/div/button[1]").click()
driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/google_selenium/images/img5.png")
#driver.quit()
act = ActionChains(driver)
#act.send_keys(Keys.ARROW_DOWN).perform()
#driver.quit()
act.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER, Keys.ENTER).perform()

