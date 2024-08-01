from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from mindrisers.pages.dashboard import DashboardPage
from mindrisers.pages.courses import CoursePage
from mindrisers.pages.post import Post
from mindrisers.pages.placement import Place
from mindrisers.pages.success_story import Success
from mindrisers.pages.admission import Admission

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()

def test_dashboard_page(driver):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open_dashboard_page("https://www.mindrisers.com.np")
    driver.maximize_window()
    time.sleep(2)
    print("Congrats, dashboard is open successfully")

def test_courses(driver):
    course_page=CoursePage(driver)
    course_page.open_page("https://www.mindrisers.com.np/courses")
    driver.maximize_window()
    time.sleep(2)
    course_page.Course_name("QA")
    course_page.click_button()
    time.sleep(2)
    course_page.click_qa()
    page_height = driver.execute_script("return document.body.scrollHeight")

    scroll_speed = 50
    scroll_iteration = int(page_height / scroll_speed)

    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(0.5)

    course_page.Enter_name("keshari bohara")
    course_page.Enter_email("keshu@gmail.com")
    course_page.Enter_number("98745623")
    course_page.Enter_subject("quality assurence")
    course_page.Enter_message("good morning")
    time.sleep(3)


def test_post_page(driver):
    post_page=Post(driver)
    post_page.open_page("https://www.mindrisers.com.np/after+2-courses")
    driver.maximize_window()
    page_height = driver.execute_script("return document.body.scrollHeight")
    scroll_speed = 50
    scroll_iteration = int(page_height / scroll_speed)
    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(0.5)


def test_placement_page(driver):
    page=Place(driver)
    page.open_page("https://www.mindrisers.com.np/placement-partner")
    driver.maximize_window()
    page_height = driver.execute_script("return document.body.scrollHeight")
    scroll_speed = 100
    scroll_iteration = int(page_height / scroll_speed)
    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(0.5)
    page.click_site()
    time.sleep(3)

def test_success_page(driver):
    success=Success(driver)
    success.open_page("https://www.mindrisers.com.np/success-gallery")
    driver.maximize_window()
    page_height = driver.execute_script("return document.body.scrollHeight")
    scroll_speed = 100
    scroll_iteration = int(page_height / scroll_speed)
    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(0.5)


def test_admission_page(driver):
    admission=Admission(driver)
    admission.open_page("https://www.mindrisers.com.np/online-admission")
    driver.maximize_window()
    admission.Enter_name("keshu")
    admission.Enter_email("keshu@gmail.com")
    admission.Enter_phone("98745612")
    admission.Enter_college("jmc")
    admission.Enter_qualification(2)
    time.sleep(2)
    admission.Enter_course(4)
    admission.Enter_shedule(1)
    admission.click_No()

    admission.Enter_query("hey")
    time.sleep(2)

