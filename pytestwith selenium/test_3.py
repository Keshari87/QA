import time

import pytest
from selenium.webdriver import Keys
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)

    yield driver
    driver.close()


@pytest.mark.parametrize("username,password",[
    ("malikacounter5","password"),
    ("invalid","password"),
    ("1","1"),
    ("abc","password"),


])
def test_login(driver,username,password):
    driver.get("https://tax.digitalpalika.org/login")
    username_field=driver.find_element(*(By.XPATH,"//input[@id='username']"))
    password_field=driver.find_element(*(By.XPATH,"//input[@id='password']"))
    login_button= driver.find_element(*(By.XPATH,"//button[normalize-space()='Login']"))

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    try:
        #check if an alert message is present
        alert=driver.switch_to.alert
        alert.accept()
        print(f"Invalid username or password for {username}")

    except:
        time.sleep(2)
        page_source=driver.page_source
        if "Counter Dashbord" in page_source:
            first = driver.find_element(By.XPATH,"//i[@class='group-hover:text-white group-focus:text-white fa-solid fa-house-chimney-window text-[1.625rem] text-[#2980b9]']")
            first.click()
            print(f" successfully login {username}")
        else:
            print(f"username or password is incorrect {username}")


            



