from selenium.webdriver.common.by import By


class ContactPage:
    def __init__(self,driver):
        self.driver=driver
        self.name=(By.XPATH,"//input[@id='name']")
        self.email = (By.XPATH, "//input[@id='email']")
        self.massege = (By.XPATH, "//textarea[@id='message']")
        self.submit = (By.XPATH, "//button[normalize-space()='Send Message']")

    def open_page(self,url):
        self.driver.get(url)

    def Enter_name(self,Name):
        self.driver.find_element(*self.name).send_keys(Name)

    def Enter_email(self, Email):
        self.driver.find_element(*self.email).send_keys(Email)

    def Enter_massege(self, Massege):
        self.driver.find_element(*self.massege).send_keys(Massege)

    def click_submit_button(self):
        self.driver.find_element(*self.submit).click()



