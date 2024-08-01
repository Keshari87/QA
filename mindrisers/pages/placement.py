from selenium.webdriver.common.by import By


class Place:
    def __init__(self, driver):
        self.driver = driver
        self.site=(By.XPATH,"//a[normalize-space()='get admission enquiry']")

    def open_page(self, url):
        self.driver.get(url)

    def click_site(self):
        self.driver.find_element(*self.site).click()