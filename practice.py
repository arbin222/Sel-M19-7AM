# from selenium import webdriver
# from time import sleep

# first program
# driver=webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com/")
# sleep(3)
# driver.maximize_window()
# sleep(3)
# # driver.minimize_window()
# # sleep(3)
# driver.find_element("xpath","//a[text()='Log in']").click()
# sleep(2)
# driver.refresh()
# sleep(3)




#second program
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/register")
sleep(2)
driver.maximize_window()
sleep(2)

#name locator
# driver.find_element("name","Gender").click()
# sleep(2)
# #id locator
# driver.find_element("id","FirstName").send_keys("Arbin")
# sleep(2)
# #class name locator
# driver.find_element("class name","single-line").send_keys("Taj")
# sleep(2)
# driver.find_element("tag name","input").click()
# sleep(3)

# link text locator
# driver.find_element("link text","Log in").click()
# sleep(3)

# partial link text locator
# driver.find_element("partial link text","og").click()
# sleep(2)

#css selector------->tagname and attribute
# driver.find_element("css selector","input[id='register-button']").click()
# sleep(2)

# xpath
# for relative xpath
# driver.find_element("xpath","//input[@id='gender-female']").click()
# sleep(2)

# for absolute xpath
# driver.find_element("xpath","")
#
# driver.close()