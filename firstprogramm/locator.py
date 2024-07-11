from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServices
from  webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set the chromedrivermanager
driver= webdriver.Chrome(service= ChromeServices(ChromeDriverManager().install()))


#get the url
website_url="https://www.mindrisers.com.np/contact-us"
#open the website
driver.get(website_url)

#maximize the window
driver.maximize_window()
time.sleep(3)

#find the form webelement by their xpath
full_name = driver.find_element(By.XPATH,"//input[@name='name']")
email = driver.find_element(By.XPATH,"//input[@name='email']")
phone =driver.find_element(By.XPATH,"//input[@name='mobile_no']")
subject= driver.find_element(By.XPATH,"//input[@name='subject']")
query = driver.find_element(By.XPATH,"//textarea[@name='message']")
button= driver.find_element(By.XPATH,"//button[@name='name']")







#fill the form
full_name.send_keys('manu')
email.send_keys('manu@gmail.com')
phone.send_keys('9856321478')
subject.send_keys('QA')
query.send_keys('its me manisha bist ')
button.click()
time.sleep(6)

driver.quit()