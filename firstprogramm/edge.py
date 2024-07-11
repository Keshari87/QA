from selenium import webdriver
from selenium.webdriver.edge.service import Service as edgeService
from webdriver_manager.microsoft  import EdgeChromiumDriverManager
import time

#set firefox driver
driver= webdriver.Edge(service= edgeService(EdgeChromiumDriverManager().install()))





#set the website
website_url= 'https://www.mindrisers.com.np/'

#get the website
driver.get(website_url)
time.sleep(3)

#maximize the window size
driver.maximize_window()
time.sleep(3)
#extract the website title

website_title= driver.title
print("website title: {website_title}")
print("congrats :code execute sucessfully")

#finally quite the driver instance
driver.quit()
