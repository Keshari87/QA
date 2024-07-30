from selenium.webdriver.common.by import By

class AboutYourselfPage:

    def __init__(self,driver):
        self.driver=driver
        self.full_name=(By.XPATH,"//input[@id='fullname']")
        self.phone=(By.XPATH,"//input[@id='phone']")
        self.email=(By.XPATH,"//input[@id='email']")
        self.hobby=(By.XPATH,"//input[@id='hobby']")
        self.summit=(By.XPATH,"//button[normalize-space()='Submit']")




    def open_page(self,url):
        self.driver.get(url)

    def enter_fullname(self,Name):
        self.driver.find_element(*self.full_name).send_keys(Name)

    def enter_phone(self,Phone):
        self.driver.find_element(*self.phone).send_keys(Phone)

    def enter_email(self,Email):
        self.driver.find_element(*self.email).send_keys(Email)
    def enter_hobby(self,Hobby):
        self.driver.find_element(*self.hobby).send_keys(Hobby)

    def click_submit_button(self):
        self.driver.find_element(*self.summit).click()


