from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from POM.pages.login_page import LoginPage
from POM.pages.dashboard_page import DashboardPage
from POM.pages.aboutyourself import AboutYourselfPage
from POM.pages.articles import Articlepage
from POM.pages.contact import ContactPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)

    yield driver
    driver.close()

# def test_login(driver):
#     login_page=LoginPage(driver)
#     login_page.open_page("https://tax.digitalpalika.org/login")
#     time.sleep(2)
#     login_page.enter_username("malikacounter5")
#     time.sleep(2)
#     login_page.enter_password("password")
#     login_page.click_login()

@pytest.mark.parametrize("username,password",[
    ("TestQA","password"),
    ("invalid","password"),
    ("1","1"),
    ("abc","password"),


])
def test_login(driver,username,password):
    login_page=LoginPage(driver)
    login_page.open_page("https://sagar-test-qa.vercel.app/")
    driver.maximize_window()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    alert_text=login_page.get_alert_text_and_accept()
    if alert_text and "invalid username or password " in alert_text:
        print(f"invalid username or password for {username}")
    else:
        if login_page.is_dashboard_present():
            print(f"Login successful for {username}")
        else:
            print(f"unexpected error or login faild for { username}")

def test_dashboard_page(driver):
    dashboard_page=DashboardPage(driver)
    dashboard_page.open_dashboard_page("https://sagar-test-qa.vercel.app/dashboard.html")
    driver.maximize_window()
    time.sleep(2)
    print("congrats dashboard is open successfully")


def test_About_yourself_page(driver):
    about_page =AboutYourselfPage(driver)
    about_page.open_page("https://sagar-test-qa.vercel.app/about.html")
    time.sleep(2)
    driver.maximize_window()
    about_page.enter_fullname("keshari")
    about_page.enter_phone("9845623145")
    about_page.enter_email("kb@gmail.com")
    about_page.enter_hobby("watching film")
    time.sleep(2)
    about_page.click_submit_button()
    time.sleep(2)
    print(f"about page visible")


def test_Article_page(driver):
    article_page =Articlepage(driver)
    article_page.open_article_page("https://sagar-test-qa.vercel.app/articles.html")
    time.sleep(2)
    driver.maximize_window()
    page_height = driver.execute_script("return document.body.scrollHeight")

    scroll_speed = 50
    scroll_iteration = int(page_height / scroll_speed)

    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
    time.sleep(0.5)


def test_contact_page(driver):
    contact_page=ContactPage(driver)
    contact_page.open_page("https://sagar-test-qa.vercel.app/contact.html")
    time.sleep(2)
    driver.maximize_window()
    contact_page.Enter_name("keshari bohara")
    contact_page.Enter_email("keshu@gmail.com")
    contact_page.Enter_massege("hey its mee")
    contact_page.click_submit_button()
    time.sleep(2)
    print("contact detail submit successfully")