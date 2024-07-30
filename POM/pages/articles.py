from selenium.webdriver.common.by import By


class Articlepage:
    def __init__(self,driver):
        self.driver=driver

    def open_article_page(self,url):
        self.driver.get(url)
