from selenium.webdriver.support import expected_conditions as  EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set the chromedriver
driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website url
website_url="https://demoqa.com/automation-practice-form"


#open the site
driver.get(website_url)

driver.maximize_window()
#calculate the height of page
page_height=driver.execute_script("return document.body.scrollHeight")

scroll_speed=200
scroll_iteration= int(page_height/scroll_speed)

#loop the iteration performance
for _ in range(scroll_iteration):
    #driver.execute_script(f"window.scrollby(0,{scroll_speed});")
    driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
    time.sleep(1)

#find the field
first_name=driver.find_element(By.XPATH,"//input[@id='firstName']")
last_name=driver.find_element(By.XPATH,"//input[@id='lastName']")
email=driver.find_element(By.XPATH,"//input[@id='userEmail']")
gender_female=driver.find_element(By.XPATH,"//label[normalize-space()='Female']")
contact=driver.find_element(By.XPATH,"//input[@id='userNumber']")
dateofbirth=driver.find_element(By.XPATH,"//input[@id='dateOfBirthInput']")
subject=driver.find_element(By.XPATH,"//input[@id='subjectsInput']")
hobbies=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//label[normalize-space()='Music']")))

#fill the element
first_name.send_keys("keshari")
last_name.send_keys("bohara")
email.send_keys("keshu@gmail.com")
gender_female.click()
contact.send_keys("12365496")
dateofbirth.send_keys("07/13/2024")
subject.send_keys("Math")
#hobbies.click()
driver.execute_script("arguments[0].click();", hobbies)
time.sleep(5)
driver.quit()
