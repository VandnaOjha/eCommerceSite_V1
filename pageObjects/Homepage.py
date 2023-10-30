from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    myaccount = "//span[contains(text(),'My Account')]"
    register_opt = "//a[contains(text(),'Register')]"
    login_opt = "Login"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.myaccount).click()
        # self.driver.find_element_by_xpath(self.myaccount).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.register_opt).click()
        # self.driver.find_element_by_link_text(self.register_opt).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.login_opt).click()
        # self.driver.find_element_by_link_text(self.login_opt).clicl()
