#path locator create and post method
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


#set the chromedriver manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#get the website url;
website_url="https://demoqa.com/alerts"

#open the website url
driver.get(website_url)

#maximize the window
driver.maximize_window()
time.sleep(2)

#alert= driver.find_element(*(By.XPATH,"//button[@id='alertButton']"))
alert =driver.find_element(*(By.XPATH,"//button[@id='confirmButton']"))
time.sleep(2)
alert.click()

time.sleep(5)
driver.quit()