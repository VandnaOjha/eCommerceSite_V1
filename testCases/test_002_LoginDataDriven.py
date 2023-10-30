import datetime
import os
import time

from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccouontPage import MyAccountPage
from utilities.logs import LogGen
from utilities.readProperties import ReadConfig
from utilities import XLutils

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
file_name = f"screenshot_{timestamp}.png"

class Test_002_LoginUser:
    baseURL = ReadConfig.getApplicationURL()
    print(baseURL)

    logger = LogGen.loggen()

    path = "D:\\eCommerceSite_V1\\testData\\usedata.xlsx"

    def test_account_reg(self, setup):
        self.logger.debug("**********Test_001_AccountRegister started.************")
        self.rows = XLutils.getRowCount(self.path,'Sheet1')
        lst_status=[]

        self.driver = setup
        self.driver.get(self.baseURL)

        self.logger.info("*****window maximize***********")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.hp = HomePage(self.driver)
        self.myAccountPage = MyAccountPage(self.driver)
        self.login = LoginPage(self.driver)

        for r in range(2,self.rows+1):

            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email = XLutils.readData(self.path,'Sheet1',r,1)
            self.password = XLutils.readData(self.path,"Sheet1",r,2)
            self.login.inputEmail(self.email)
            time.sleep(1)
            self.login.inputPassword(self.password)
            time.sleep(1)
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots" + file_name)
            self.login.clickLoginBtn()
            time.sleep(1)

            self.targetPage = self.login.myAccountExists()
            if self.targetPage==True:
                assert True
            else:
                self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots"+"\\test_login")
                assert False

            self.myAccountPage.clickMyAccount()
            self.myAccountPage.clickLogout()

        self.logger.info("........End of test case.**********8")


