import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import chrome

from pageObject.Customer import Customer
from pageObject.HomePage import HomePage
from pageObject.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.LoggingUtility import GenerateLogs
from utilities.ExcelUtility import ExcelReader
from BasePage.BasePage import BasePage
import pytest
import time


class Test0001:
    import allure
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = GenerateLogs.log_gen(__name__)
    path = "C:/Users/HP/PycharmProjects/pythonFrameWork/TestData/Excel.xlsx"

    @allure.description("verify exiting customer record")
    @allure.epic("verify exiting customer record in epic")
    @allure.severity(allure.severity_level.NORMAL)
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

        self.ip.loginPage(self.username, self.password)
        self.logger.info("entered valid username and password")

        self._basePage.closeBrowser()

        self._homePage.clickOnLeftPanel()
        self.logger.info("click on customer on left panel")
        self._customer.verifyExisting(self.customer)
        self.logger.info("verify existing customer details")
        self._basePage.closeBrowser()
        self.logger.info("***********END TC 001*********** ")

    @allure.description("verify home-page title")
    @allure.epic("verify home-page title in epic")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_VerifyHomePageTitle(self, setUp):
        self.logger.info("***************Start TC 002 **************************")
        self.logger.info("*********** verify Home page title *********** ")
        self.driver = setUp

        self.ip = LoginPage(self.driver)
        self._basePage = BasePage(self.driver)
        self._homePage = HomePage(self.driver)
        self._customer = Customer(self.driver)

        print("-----------------------test_VerifyHomePageTitle----------------------------")

        self.logger.info("************* Enter the Url for   ************")
        self.driver.get(self.baseUrl)
        self.ip.loginPage(self.username, self.password)
        self.logger.info("entered valid username and password")
        time.sleep(4)
        pageTitle = self._basePage.getTitle()
        self.logger.info("captured page title")
        print(pageTitle)
        time.sleep(4)
        if pageTitle == "Dashboard / nopCommerce administration123":
            assert True
            self.logger.info("verified Page title is capture correct ")
            # self._basePage.closeBrowser()
        else:
            # time.sleep(4)
            # self.driver.save_screenshot("..\\screenShot\\" + "test_homePageTile001.png")
            # self.driver.save_screenshot("C://Users//HP//PycharmProjects//pythonFrameWork//screenShot//" + "test_homePageTile00123.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="failed to verify title",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("verified Page title is not capture correct ")

            # time.sleep(4)
            self.logger.info("***************End TC 2 **************************")
            assert False

    @allure.description("verify new customer is created ")
    @allure.epic("verify new customer is created in epic")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_VerifyNewCustomerIsCreated(self, setUp):
        self.logger.info("*********** Start TC 003*********** ")
        self.logger.info("*********** verify new customer is created *********** ")
        self.driver = setUp

        print("-----------------------test_VerifyNewCustomerIsCreated----------------------------")
        self.ip = LoginPage(self.driver)
        self._basePage = BasePage(self.driver)
        self._homePage = HomePage(self.driver)
        self._customer = Customer(self.driver)
        self.logger.info("************* Enter the Url for   ************")
        self.driver.get(self.baseUrl)

        self.ip.loginPage(self.username, self.password)
        self.logger.info("entered valid username and password")
        time.sleep(4)

        self.logger.info("click on customer on left panel")
        self._homePage.clickOnLeftPanel()
        time.sleep(4)

        self.logger.info("click on new button and enter all details and click on save button ")
        self._customer.createdNewCustomer()

        self._basePage.closeBrowser()
        self.logger.info("***************End TC 003 **************************")
