cd="C:\\Users\\Pranati\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
from selenium import webdriver
import time
browser=webdriver.Chrome(cd)
browser.get("https://www.facebook.com/login")
time.sleep(5)
un=browser.find_element_by_xpath('//input[@id="email"]')
un1=input("Enter the Username")
un.send_keys(un1)
pswrd=browser.find_element_by_xpath('//input[@id="pass"]')
pswrd1=input("Enter Passord")
pswrd.send_keys(pswrd1)
login=browser.find_element_by_xpath('//button[@id="loginbutton"]')
login.click()