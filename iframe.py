from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demoapps.qspiders.com/ui/frames?sublist=0")

webdriver=driver.find_element("xpath","//iframe[@class='w-full h-96']")
driver.switch_to.frame(webdriver)

driver.find_element("id","username").send_keys("arbin")
driver.find_element("id","password").send_keys("1234")
sleep(1)


driver.switch_to.parent_frame()
driver.find_element("xpath","//section[text()='Synchronization']").click()
sleep(3)

driver.close()