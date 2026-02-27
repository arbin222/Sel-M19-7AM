from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()


sleep(3)

driver.find_element(("xpath","//a[text()='Twitter']").click()
sleep(3)

windows = driver.window_handles
driver.switch_to.window(windows[1])
print(driver.title)

driver.close()
sleep(3)
driver.switch_to


