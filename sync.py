from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome()
# Implicit wait
# driver.implicitly_wait(5)
driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()

# driver.find_element("id","Email").send_keys('arbintaj125@gmail.com')
# driver.find_element("id","Password").send_keys('Arbin@2005')
# driver.find_element("xpath" ,"/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[4]/label").click()
# driver.find_element("xpath", "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input").click()
# sleep(3)


# explicit wait
# my_wait=WebDriverWait(driver,10, poll_frequency=4)
# tagnames = my_wait.until(EC.presence_of_all_elements_located(('tag name', 'a')))
# for tags in tagnames:
#     print(tags.text)
# # my_wait.until(EC.visibility_of_element_located(('id', 'Email'))).send_keys("arbintaj125@gmail.com")
# my_wait.until(EC.visibility_of_element_located(('id', 'Password'))).send_keys("Arbin@2005")
# sleep(3)
# driver.close()





