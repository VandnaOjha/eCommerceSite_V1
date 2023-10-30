import time
from pageObjects.AccountRegistrationPage import AccountRegisterPage
from pageObjects.Homepage import HomePage
from utilities import randomeString
from utilities.logs import LogGen
from utilities.readProperties import ReadConfig


class Test_001_AccountRegister:
    baseURL = ReadConfig.getApplicationURL()
    print(baseURL)

    logger = LogGen.loggen() 

    def test_account_reg(self, setup):
        self.logger.debug("**********Test_001_AccountRegister started.************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.logger.info("*****window maximize***********")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.registerPg = AccountRegisterPage(self.driver)
        self.registerPg.setFirstName("Testing")
        self.registerPg.setLastName("Account")
        self.email = randomeString.random_string_generator() + '@gmail.com'
        self.registerPg.setEmail(self.email)
        self.registerPg.setPassword("test@123")
        self.driver.execute_script("window.scrollTo(0,800)")
        time.sleep(3000)

        # button_1 = self.registerPg.clickContinueButton()
        # button_1.click()
        # self.driver.execute_script("arguments[0].scrollIntoView();", button_1)
        # self.driver.execute_script("arguments[0].click();", button_1)
        # self.registerPg.clickAgree()
        # self.driver.execute_script("arguments[0].click();", self.registerPg.clickContinueButton())
        # self.registerPg.clickContinueButton()
