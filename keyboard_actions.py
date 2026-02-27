from selenium import webdriver
from time import sleep
from selenium .webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.implicitly_wait(6)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)

Name=driver.find_element("id","name")
Name.send_keys("Arbin")
Name.send_keys(Keys.CONTROL+'a')
Name.send_keys(Keys.CONTROL+'c')

Email=driver.find_element("id","email")
Email.send_keys(Keys.CONTROL+'v')
sleep(3)

Email.send_keys(Keys.CONTROL+'a')
sleep(1)
Email.send_keys(Keys.DELETE)
sleep(2)
driver.close()
