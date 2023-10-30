from selenium import webdriver
from selenium.webdriver.common.by import By


class MyAccountPage:
    myaccount_xpath = "//span[contains(text(),'My Account')]"
    logout_xpath = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.myaccount_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.logout_xpath).click()