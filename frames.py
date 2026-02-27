from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")
sleep(3)

driver.switch_to.frame("singleframe")
driver.find_element("xpath","//input[@type='text']").send_keys("Selenium")
sleep(3)

driver.switch_to.parent_frame()
driver.find_element("xpath","//a[text()='Iframe with in an Iframe']").click()
sleep(3)


nested=driver.find_element('xpath',"//iframe[@src='MultipleFrames")
driver.switch_to.frame(nested)
print(driver.find_element('tag name','h5').text)


single=driver.find_element('xpath',"//iframe[@src='SingleFrame")
driver.switch_to.frame(single)
print(driver.find_element('tag name','h5').text)
sleep(3)

driver.find_element("xpath","//input[@type='text']").send_keys("python")
sleep(3)

driver.switch_to.default_content()
driver.find_element("xpath","//a[text()='Single Iframe']").click()
sleep(3)

driver.close()

driver.close()