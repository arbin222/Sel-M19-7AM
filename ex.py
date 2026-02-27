from selenium import webdriver
from selenium.webdriver.support.select import Select
import openpyxl
from ex_ut import *
from time import sleep
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(4)
file=r"C:\Users\Levono\OneDrive\Desktop\Assigmentpy.xlsx"
rows=get_row_count(file,"sheet1")
for row in range(2,rows+1):
    p=readData(file,"sheet1",row,1)
    a=readData(file,"sheet1",row,2)
    b=readData(file, "sheet1", row, 3)
    c=readData(file, "sheet1", row, 4)
    d=readData(file, "sheet1", row, 5)
    e=readData(file, "sheet1", row, 6)
    f=readData(file, "sheet1", row, 7)
    g=readData(file, "sheet1", row, 8)
    print(p,a,b,c,d,e,f,g)

    driver.find_element("id","name").send_keys(p)
    driver.find_element("id","email").send_keys(a)
    driver.find_element("id","phone").send_keys(b)

driver.close()







