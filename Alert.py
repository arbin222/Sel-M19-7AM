from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.implicitly_wait(6)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)

#Simple alert
# driver.find_element("id","alertBtn").click()
# sleep(3)
# var=driver.switch_to.alert
# print(var.text)
# var.accept()

#for confirmation alert
driver.find_element("id","confirmBtn").click()
var=driver.switch_to.alert
sleep(3)
print(var.text)
var.accept()
p=driver.find_element("id","demo")
print(p.text)



driver.close()


