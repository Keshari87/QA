from selenium.webdriver.common.by import By

class CoursePage:
    def __init__(self,driver):
        self.driver=driver
        self.search=(By.XPATH,"//input[@name='searchTerm']")
        self.button= (By.XPATH,"//button[@class='btn-simple']")
        self.section= (By.XPATH,"//a[@href='/courses/quality-assurance-training-in-nepal']//img[@class='mb-5']")
        self.name=(By.XPATH,"//input[@placeholder='Name']")
        self.email=(By.XPATH,"//input[@placeholder='Email']")
        self.number=(By.XPATH,"//input[@placeholder='Mobile Number']")
        self.subject=(By.XPATH,"//input[@placeholder='Subject']")
        self.message=(By.XPATH,"//textarea[@placeholder='Message']")



    def open_page(self,url):
        self.driver.get(url)

    def Course_name(self,Name):
        self.driver.find_element(*self.search).send_keys(Name)

    def click_button(self):
        self.driver.find_element(*self.button).click()

    def click_qa(self):
        self.driver.find_element(*self.section).click()

    def Enter_name(self,Name):
        self.driver.find_element(*self.name).send_keys(Name)

    def Enter_email(self,Email):
        self.driver.find_element(*self.email).send_keys(Email)

    def Enter_number(self,Number):
        self.driver.find_element(*self.number).send_keys(Number)

    def Enter_subject(self,Subject):
        self.driver.find_element(*self.subject).send_keys(Subject)

    def Enter_message(self,Message):
        self.driver.find_element(*self.message).send_keys(Message)

