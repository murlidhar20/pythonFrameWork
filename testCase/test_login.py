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
    @allure.epic("verify exiting customer record")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    @pytest.mark.depends(on=['test_welcome_to_home_Page'])
    def test_verify_existing_customer(self, setUp):
        self.logger.info("*********** Start verify existing customer details *********** ")

        self.driver = setUp
        self.ip = LoginPage(self.driver)
        self._basePage = BasePage(self.driver)
        self._homePage = HomePage(self.driver)
        self._customer = Customer(self.driver)

        self.customer = ExcelReader.read_data(self.path, "Sheet1", 2, 4)
        self.driver.get(self.baseUrl)
        self.logger.info("************* Entered the Url  ************")

        self.ip.login_page(self.username, self.password, "Dashboard / nopCommerce administration")
        self.logger.info("entered valid username and password")

        self._homePage.click_on_left_panel()
        self.logger.info("clicked on customer on left panel")

        self._customer.verify_existing(self.customer)
        self.logger.info("verified existing customer details")

        self._basePage.close_browser()
        self.logger.info("closed the browser")

        self.logger.info("*********** END verify existing customer details*********** ")

    @allure.description("verify home-page title")
    @allure.epic("verify home-page title")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.depends(on=['test_verify_existing_customer'])
    def test_verify_homePage_title(self, setUp):
        self.logger.info("***********  start verify Home page title *********** ")

        self.driver = setUp
        self.ip = LoginPage(self.driver)
        self._basePage = BasePage(self.driver)
        self._homePage = HomePage(self.driver)
        self._customer = Customer(self.driver)

        self.driver.get(self.baseUrl)
        self.logger.info("************* Enter the Url for   ************")
        self.ip.login_page(self.username, self.password, "Dashboard / nopCommerce administration")

        self.logger.info("entered valid username and password")
        time.sleep(4)
        pageTitle = self._basePage.get_title()
        self.logger.info("captured page title")
        print(pageTitle)
        time.sleep(4)
        if pageTitle == "Dashboard / nopCommerce administration1234":
            assert True
            self.logger.info("verified Page title is capture correct ")
            # self._basePage.closeBrowser()
        else:
            # time.sleep(4)
            # self.driver.save_screenshot("..\\screenShot\\" + "test_homePageTile001.png")
            # self.driver.save_screenshot("C://Users//HP//PycharmProjects//pythonFrameWork//screenShot//" + "test_homePageTile00123.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="failed to verify title",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("verified user is not navigated to home page")

            # time.sleep(4)
            assert False
        self._basePage.close_browser()
        self.logger.info("closed the browser")
        self.logger.info("***********END verify Home page title ***********")

    @allure.description("verify new customer is created ")
    @allure.epic("verify new customer is created ")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_verify_new_customer_is_created(self, setUp):
        self.logger.info("*********** verify new customer is created *********** ")

        self.driver = setUp
        self.ip = LoginPage(self.driver)
        self._basePage = BasePage(self.driver)
        self._homePage = HomePage(self.driver)
        self._customer = Customer(self.driver)

        emailId = "Murl1889988889@HP.com"
        password = "12j345678"
        firstName = "Mukkrli"
        lastName = "dhkkhar"
        companyName = "HP"
        successMessage = "The new customer has been added successfully."

        self.driver.get(self.baseUrl)
        self.logger.info("************* Enter the Url for   ************")

        self.ip.login_page(self.username, self.password, "Dashboard / nopCommerce administration")
        self.logger.info("entered valid username and password")
        time.sleep(4)

        self._homePage.click_on_left_panel()
        self.logger.info("clicked on customer on left panel")
        time.sleep(4)

        self._customer.created_new_customer(emailId, password, firstName, lastName, companyName, successMessage)
        self.logger.info("click on new button and enter all details and click on save button ")

        self._basePage.close_browser()
        self.logger.info("closed the browser")
        self.logger.info("***********END verify Home page title ***********")

    @allure.description("verify regression TC")
    @allure.epic("verify regression TC")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_regression(self):
        self.logger.info("*************** Start test_regression **************************")
        self.logger.info("*************** End test_regression **************************")

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    @pytest.mark.skip
    def test_skipped(self):
        self.logger.info("*************** Start test_Skipped **************************")
        self.logger.info("*************** End test_Skipped  **************************")

    @allure.description("verify verify home page")
    @allure.epic("verify home page")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_welcome_to_home_Page(self):
        self.logger.info("*************** Start test_welcome_to_home_Page **************************")
        print("Welcome to test_welcome_to_home_Page")
        self.logger.info("*************** END test_welcome_to_home_Page **************************")


'''
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
        
        '''
