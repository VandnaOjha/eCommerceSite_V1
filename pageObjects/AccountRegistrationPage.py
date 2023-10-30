from selenium.webdriver.common.by import By


class AccountRegisterPage:
    firstname_name = "firstname"
    lastname_name = "lastname"
    email_name = "email"
    password_name = "password"
    agree_popup_name = "//*[@type='checkbox']"
    continue_btn = "//button[contains(text(),'Continue')]"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        self.driver.find_element(By.NAME, self.firstname_name).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.NAME, self.lastname_name).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.email_name).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.password_name).send_keys(pwd)

    def clickAgree(self):
        self.driver.find_element(By.XPATH, self.agree_popup_name).click()

    def clickContinueButton(self):
        button = self.driver.find_element(By.XPATH, self.continue_btn)
        return button
        # self.driver.find_element(By.XPATH, self.continue_btn).click()
