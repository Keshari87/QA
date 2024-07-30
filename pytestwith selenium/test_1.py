import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def testmethod1():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    #set website
    website_url=driver.get("https://google.com")
    search=driver.find_element(*(By.XPATH,"//textarea[@id='APjFqb']"))
    search.send_keys("mindrisers.com.np")
    search.send_keys(Keys.RETURN)
    time.sleep(3)
    #click on the available link
    first_link=driver.find_element(By.XPATH,"//h3[contains(text(),'Best IT Training Institute in kathmandu, Nepal | M')]")
    first_link.click()
    time.sleep(2)
    print("this is first method")

def testmethod2():
    print("this is second method")
