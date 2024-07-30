from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


#set the driver
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#set the url
driver.get("https://merolagani.com/NewsList.aspx")

driver.maximize_window()

#driver.maximize_window()
time.sleep(2)
market=driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))

market.click()
time.sleep(3)
driver.quit()