from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Admission:

    def __init__(self,driver):
        self.driver=driver
        self.name=(By.XPATH,"//input[@id='full_name']")
        self.email=(By.XPATH,"//input[@id='email']")
        self.phone=(By.XPATH,"//input[@id='mobile_no']")
        self.college=(By.XPATH,"//input[@id='college']")
        self.qualification=(By.XPATH,"//select[@id='qualification']")
        self.course=(By.XPATH,"//select[@id='course']")
        self.schedule=(By.XPATH,"//select[@id='shedule']")
        self.yesno=(By.XPATH,"//label[normalize-space()='No']")
        self.query=(By.XPATH,"//textarea[@id='question']")



    def open_page(self,url):
        self.driver.get(url)


    def Enter_name(self,Name):
        self.driver.find_element(*self.name).send_keys(Name)

    def Enter_email(self,Email):
        self.driver.find_element(*self.email).send_keys(Email)

    def Enter_phone(self,Phone):
        self.driver.find_element(*self.phone).send_keys(Phone)

    def Enter_college(self,College):
        self.driver.find_element(*self.college).send_keys(College)

    def Enter_qualification(self,Qua):
         Select(self.driver.find_element(*self.qualification)).select_by_index(Qua)



    def Enter_course(self,Course):
        Select( self.driver.find_element(*self.course)).select_by_index(Course)

    def Enter_shedule(self,Schedule):
         Select(self.driver.find_element(*self.schedule)).select_by_index(Schedule)

    def click_No(self):
        self.driver.find_element(*self.yesno).click()

    def Enter_query(self,Query):
        self.driver.find_element(*self.query).send_keys(Query)
