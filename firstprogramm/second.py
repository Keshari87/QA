from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServices
from  webdriver_manager.chrome import ChromeDriverManager
import time

#set the chromedrivermanager
driver= webdriver.Chrome(service= ChromeServices(ChromeDriverManager().install()))

#set the website
website_url= 'https://www.mindrisers.com.np/'

#get the website
driver.get(website_url)
time.sleep(3)

#maximize the window size
driver.maximize_window()
time.sleep(3)

#calculate the height of the webpage
#page_height= driver.execute_script("return document,body,scrollheight")
#scroll down the contents
page_height = driver.execute_script("return Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);")

scroll_speed=500
scroll_iterations=int(page_height/scroll_speed)

#loop the iteration performance
for _ in range(scroll_iterations):
    #driver.execute_script(f"window.scrollby(0,{scroll_speed});")
    driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
    time.sleep(1)

#print the title
    website_title = driver.title
    print("website title: {website_title}")
    print("code run successfully")

driver.quit()

