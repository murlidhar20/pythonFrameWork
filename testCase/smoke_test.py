from allure_commons.types import AttachmentType
from selenium.webdriver import chrome
import pytest
import time
import allure
from selenium.webdriver.common.by import By

from pageObject.Customer import Customer
from pageObject.HomePage import HomePage
from pageObject.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.LoggingUtility import GenerateLogs
from utilities.ExcelUtility import ExcelReader
from BasePage.BasePage import BasePage

from pageObject.product_search_page import product_search_page
from pageObject.my_account_page import my_account_page

import allure


class Test0001:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = GenerateLogs.log_gen(__name__)
    path = "C:/Users/HP/PycharmProjects/pythonFrameWork/TestData/Excel.xlsx"




    @allure.description("verify user is able to search product in global search")
    @allure.epic("verify user is able to search product in global search")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test001_user_is_able_to_search_product_in_global_search(self, setUp):
        self.logger.info(" Start : verify user is able to search product in global search ")

        # page object creation
        self.driver = setUp
        self.login_page = LoginPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.customer = Customer(self.driver)
        self.product_search = product_search_page(self.driver)

        # Test Data
        self.customer = ExcelReader.read_data(self.path, "Sheet1", 2, 4)
        product_name = "mobile phone"

        self.logger.info("Enter the Url")
        self.driver.get(self.baseUrl)

        self.logger.info("entered valid username and password")
        self.login_page.login_to_application(self.username, self.password)

        self.logger.info("fresh button is available")
        self.home_page.verify_fresh_button_is_displayed()

        self.logger.info("entered product ")
        self.product_search.enter_the_product(product_name)

        self.logger.info("user is able to logout")
        self.login_page.log_out()

        self.logger.info("closed the browser")
        self.base_page.close_browser()

        self.logger.info(" END : verify user is able to search product in global search ")





    @allure.description("user is able to add the product if brand and price filter is applied")
    @allure.epic("user is able to add the product if brand and price filter is applied")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test002_user_is_able_to_Add_the_Product_if_brand_and_price_Filer_is_applied(self, setUp):
        self.logger.info("Start : TC user is able to add the product if brand and price filter is applied-")

        # page object creation
        self.driver = setUp
        self.login_page = LoginPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.customer = Customer(self.driver)
        self.product_search = product_search_page(self.driver)

        # Test Data
        self.customer = ExcelReader.read_data(self.path, "Sheet1", 2, 4)
        product_name = "mobile phone"
        brand_name = "Oppo"
        price_range = "₹10,000 - ₹20,000"

        self.logger.info("Enter the Url")
        self.logger.info("Enter the Url")
        self.logger.info("Enter the Url")
        self.driver.get(self.baseUrl)

        self.logger.info("entered valid username and password")
        self.login_page.login_to_application(self.username, self.password)

        self.logger.info("fresh button is available")
        self.home_page.verify_fresh_button_is_displayed()

        self.logger.info("entered product ")
        self.product_search.enter_the_product(product_name)

        self.logger.info("entered Brand ")
        self.product_search.click_on_any_brand(brand_name)

        self.logger.info("select range")
        self.product_search.click_on_any_range(price_range)

        self.logger.info("click on first product")
        self.product_search.click_on_first_product()

        self.logger.info("clicked on close button on pop-up")
        self.product_search.click_on_close_button()

        self.logger.info("user is able to logout")
        self.login_page.log_out()

        self.logger.info("closed the browser")
        self.base_page.close_browser()

        self.logger.info("END : TC user is able to add the product if brand and price filter is applied-")



    @allure.description("user can delete the product from add to card list")
    @allure.epic("user can delete the product from add to card list")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    @pytest.mark.depends(on=['test002_user_is_able_to_Add_the_Product_if_brand_and_price_Filer_is_applied'])
    def test003_user_can_delete_the_product_from_add_to_card_list(self, setUp):
        self.logger.info("Start TC  : user can delete the product from add to card list")

        # page object creation
        self.driver = setUp
        self.login_page = LoginPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.customer = Customer(self.driver)
        self.product_search = product_search_page(self.driver)

        # Test Data
        self.customer = ExcelReader.read_data(self.path, "Sheet1", 2, 4)

        self.logger.info("Enter the Url")
        self.driver.get(self.baseUrl)

        self.logger.info("entered valid username and password")
        self.login_page.login_to_application(self.username, self.password)

        self.logger.info("fresh button is available")
        self.home_page.verify_fresh_button_is_displayed()

        self.logger.info("delete the product")
        self.product_search.delete_the_product()

        self.logger.info("user is able to logout")
        self.login_page.log_out()

        self.logger.info("closed the browser")
        self.base_page.close_browser()

        self.logger.info("END TC  : user can delete the product from add to card list ")
        

        

        



    
    @allure.description("user is able to view balance and add money")
    @allure.epic("user is able to view balance and add money")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test004_user_is_view_balance_and_add_money(self, setUp):
        self.logger.info("Start TC  : user is able to view balance and add money")

        # page object creation
        self.driver = setUp
        self.login_page = LoginPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.customer = Customer(self.driver)
        self.product_search = product_search_page(self.driver)
        self.account_page = my_account_page(self.driver)

        # Test Data
        self.customer = ExcelReader.read_data(self.path, "Sheet1", 2, 4)
        self.amount = "10000"

        self.logger.info("Enter the Url")
        self.driver.get(self.baseUrl)

        self.logger.info("entered valid username and password")
        self.login_page.login_to_application(self.username, self.password)

        self.logger.info("fresh button is available")
        self.home_page.verify_fresh_button_is_displayed()

        self.logger.info("fresh button is available")
        self.home_page.click_on_account_list_header()

        self.logger.info("view amazon pay balance")
        self.account_page.view_amazon_pay_balance()

        self.logger.info("add money to wallet")
        self.account_page.add_money(self.amount)

        self.base_page.back()

        self.logger.info("user is able to logout")
        self.login_page.log_out()

        self.logger.info("closed the browser")
        self.base_page.close_browser()

        self.logger.info("END TC  : user is able to view balance and add money ")

    @allure.description("user is able to edit address")
    @allure.epic("user is able to edit address")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test005_user_is_able_to_edit_address(self, setUp):
        self.logger.info("Start TC  : user is able to edit address")

        # page object creation
        self.driver = setUp
        self.login_page = LoginPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.customer = Customer(self.driver)
        self.product_search = product_search_page(self.driver)
        self.account_page = my_account_page(self.driver)

        self.base_page.implicitly_waits(120);
        self.logger.info("Enter the Url")
        self.driver.get(self.baseUrl)

        self.logger.info("entered valid username and password")
        self.login_page.login_to_application(self.username, self.password)

        self.logger.info("fresh button is available")
        self.home_page.verify_fresh_button_is_displayed()

        self.logger.info("click on account list ")
        self.home_page.click_on_account_list_header()

        self.logger.info("click on  address and verify edit button")
        self.account_page.click_on_address_and_verify_edit_button()

        self.logger.info("user is able to logout")
        self.login_page.log_out()

        self.logger.info("closed the browser")
        self.base_page.close_browser()

        self.logger.info("END TC  :  user is able to edit address ")
        

        

