cd="C:\\Users\\Pranati\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
from selenium import webdriver
browser=webdriver.Chrome(cd) # To create a connection between the code and google chrome.
browser.get("https://www.linkedin.com/login") # To open the link.
un=browser.find_element_by_xpath('//input[@id="username"]') #locate the element and click
un.send_keys("=======") #send input to that linkedin login id
passwrd=browser.find_element_by_xpath('//input[@id="password"]')
passwrd.send_keys("=======") #send your linkedin profile password to that.
sign_in=browser.find_element_by_xpath('//button[@class="btn__primary--large from__button--floating mercado-button--primary"]')
sign_in.click( )