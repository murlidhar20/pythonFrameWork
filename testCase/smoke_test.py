from allure_commons.types import AttachmentType
from selenium.webdriver import chrome
import pytest
import time
import allure
from pageObject.Customer import Customer
from pageObject.HomePage import HomePage
from pageObject.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.LoggingUtility import GenerateLogs
from utilities.ExcelUtility import ExcelReader
from BasePage.BasePage import BasePage
import allure


class Test0001:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = GenerateLogs.log_gen(__name__)
    path = "C:/Users/HP/PycharmProjects/pythonFrameWork/TestData/Excel.xlsx"

    @allure.description("verify exiting customer record")
    @allure.epic("verify exiting customer record in epic")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    # @pytest.mark.depends(on=['test_welcome_to_home_Page'])
    def test_VerifyExistingCustomer(self, setUp):
        self.logger.info("*********** Start TC 001*********** ")
        self.logger.info("*********** verify existing customer details *********** ")

        self.driver = setUp

        self.ip = LoginPage(self.driver)
        self._basePage = BasePage(self.driver)
        self._homePage = HomePage(self.driver)
        self._customer = Customer(self.driver)

        print("-----------------------test_VerifyExistingCustomer----------------------------")

        self.customer = ExcelReader.read_data(self.path, "Sheet1", 2, 4)

        print(self.customer)

        self.logger.info("************* Enter the Url  ************")
        self.driver.get(self.baseUrl)

        self.ip.login_to_application(self.username, self.password)
        self.logger.info("entered valid username and password")
        

