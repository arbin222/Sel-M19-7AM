# print('hello world')

# a=int(input("Enter the maximum range: "))
# for i in range(a+1):
#     a=len(str(i))
#     s=0
#     t=i
#     while i>0:
#         rem=i%10
#         s=s+(rem**a)
#         i=i//10
#     if s==t:
#          print(t)


# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com/")
# sleep(3)
# driver.maximize_window()
# sleep(2)
# # driver.minimize_window()
# # sleep(3)
# driver.find_element("xpath","//a[text()='Log in']").click()
# sleep(2)
# driver.back()
# sleep(3)
# driver.forward()
# sleep(3)
# driver.refresh()
# sleep(3)
# driver.close()

from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
sleep(3)

#locator matching with one element
print(driver.find_element("id","Email"))
print(driver.find_elements("id","Email"))

#locator matching with  n number of we elements
print(driver.find_element("tag name","a"))
print(driver.find_elements("tag name","a"))

#locators matching with 0 elements
print(driver.find_element("id","mail"))
print(driver.find_elements("id","mail"))

# driver.close()

