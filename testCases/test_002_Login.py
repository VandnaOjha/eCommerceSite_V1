import os
import time

from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.logs import LogGen
from utilities.readProperties import ReadConfig


class Test_002_LoginUser:
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
        self.hp.clickLogin()

        self.login = LoginPage(self.driver)
        # self.login = LoginPage(self.driver)cls
        self.login.inputEmail()
        self.login.inputPassword()
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots" + "\\login_page.png")
        self.login.clickLoginBtn()
        time.sleep(3000)

        self.targetPage = self.login.myAccountExists()
        if self.targetPage==True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots"+"\\test_login")
            assert False

        self.logger.info("........End of test case.**********8")


