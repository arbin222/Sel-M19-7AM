from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)

no_of_rows=len(driver.find_elements("xpath","//table[@name='BookTable']//tr"))
no_of_columns=len(driver.find_elements("xpath", "//table[@name='BookTable']//tr/th"))
print(no_of_rows,no_of_columns)
for row in range(2,no_of_rows+1):
     for col in range(1,no_of_columns+1):
         print(driver.find_element("xpath",f"//table[@name='BookTable']//tr[{row}]/td[{col}]").text,end='   ')
     print()

driver.quit()