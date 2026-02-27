from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
driver.get("https://demowebshop.tricentis.com/")

sleep(3)

# driver.find_element("id","Email").send_keys("arbin")
# sleep(3)
# driver.find_element("class name","_6luy._55r1._1kb2._nyh").send_keys("arbin@123")
# sleep(3)
# driver.find_element("name","pass").send_keys()
# sleep(3)

# xpath absolute with single slash and full path6
# driver.find_element("xpath" ,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]").send_keys("testing")
# sleep(3)
# driver.find_element("xpath","//*[@id='Wikipedia1_wikipedia-search-input']").send_keys("SELENIUM")



# driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[1]/div[1]")
# driver.find_element("xpath","//*[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
# driver.find_element("xpath", "//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input").click()
# sleep(3)




