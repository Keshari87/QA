
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#set the chromedriver manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#open url
driver.get("https://www.sharesansar.com/agm-list")

driver.maximize_window()
target_y=6000
scroll_distance =1000
current_y=0

#loop the scrolling
while current_y< target_y:
    driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

#market= driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))
#market.click()

#link=driver.find_element(By.LINK_TEXT,'AGM/SGM')
#link.click()
time.sleep(2)
next = driver.find_element(*(By.XPATH, "//a[@id='myTableC_next']"))
i=1
while (i<34):
    next.click()
    i=i+1
time.sleep(2)
print("run successfully")
driver.quit()