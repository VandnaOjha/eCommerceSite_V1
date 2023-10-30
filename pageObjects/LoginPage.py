from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    email_xpath = "//input[@id='input-email']"
    pwd_xpath = "//input[@id='input-password']"
    loginBtn_xpath = "//button[contains(text(),'Login')]"
    myaccount_xpath = "//h2[contains(text(),'My Account')]"

    def __init__(self, driver):
        self.driver = driver

    def inputEmail(self,email):
        # self.driver.find_element(By.XPATH, self.email_xpath).send_keys('vannuojha09@gmail.com')
        self.driver.find_element(By.XPATH, self.email_xpath)

    def inputPassword(self,password):
        # self.driver.find_element(By.XPATH, self.pwd_xpath).send_keys('vandu@15')
        self.driver.find_element(By.XPATH, self.pwd_xpath)

    def clickLoginBtn(self):
        # self.driver.find_element(By.XPATH, self.loginBtn_xpath).click()
        self.driver.find_element(By.XPATH, self.loginBtn_xpath).click()

    def myAccountExists(self):
        try:
            self.driver.find_element(By.XPATH, self.myaccount_xpath).is_displayed()
        except:
            return False
