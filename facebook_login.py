cd="C:\\Users\\Pranati\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"

from selenium import webdriver
import time
browser=webdriver.Chrome(cd)
time.sleep(2)
browser.get("https://www.facebook.com/login")
time.sleep(5)
un=browser.find_element_by_xpath('//input[@id="email"]')
un.send_keys("=======")  #Here you have to put your user id
pswrd=browser.find_element_by_xpath('//input[@id="pass"]')
pswrd.send_keys("===========")	#Here you have to put your profile password
login=browser.find_element_by_xpath('//button[@id="loginbutton"]')
login.click() 