import allure
from selenium.webdriver.common.by import By

from BasePage.BasePage import BasePage
import time
from utilities.AllureCaptureScreenShot import GetScreenShot


class HomePage:
    text_userName_xpath = (By.NAME, "Email")
    text_passWord_xpath = (By.ID, "Password")
    button_login_xpath = (By.XPATH, "//*[text()='Log in']")
    button_MainCustomer = (
        By.XPATH, "(//li[@class='nav-item has-treeview']/descendant::p[contains(text(),'Customers')])[1]")
    button_ChildCustomer = (By.XPATH, "//ul[@class='nav nav-treeview'][@style='display: block;']/li[1]/a/p")
    lk_homePage_xpath = (By.XPATH, "//*[@id='nav-xshop']/a")
    lk_Fresh_xpath = (By.XPATH, "//*[@id='nav-xshop']/a[text()='Fresh']")
    tbox_globalSearch_xpath = (By.XPATH, "//*[@id='twotabsearchtextbox']")
    btn_searchSubmit_xpath = (By.XPATH, "//*[@id='nav-search-submit-button']")
    btn_result_xpath = (By.XPATH, "//*[text()='RESULTS']")
    header_signIn_xpath = (By.XPATH, "//*[@class='nav-line-1-container']")
    header_homePage_xpath = (By.XPATH, "(//*[@class='nav-progressive-content'])[@id='nav-xshop']/a")
    btn_yourAddress_xpath = (By.XPATH, "//h2[contains(text(), ' Your Addresses')]")
    btn_yourAddressEdit_xpath = (By.XPATH, "(//*[contains(text(),'Edit')])[1]")

    def __init__(self, driver):
        self.screenShotPage = None
        self.BasePage = None
        self.driver = driver

    # @allure.step("click on left panel ")
    # def click_on_left_panel(self):
    #     self.BasePage = BasePage(self.driver)
    #     time.sleep(1)
    #     self.BasePage.element_click(self.button_MainCustomer)
    #     time.sleep(2)
    #     self.BasePage.element_click(self.button_ChildCustomer)

    @allure.step("verify fresh button is displayed")
    def verify_fresh_button_is_displayed(self):
        try:
            self.BasePage = BasePage(self.driver)
            self.screenShotPage = GetScreenShot(self.driver)
            if self.BasePage.verify_element_is_displayed(self.lk_Fresh_xpath):
                self.screenShotPage.getScreenShot("fresh button in home page is displayed")
                assert True
            else:
                self.screenShotPage.getScreenShot("fresh button in home page  is not displayed")
                assert False
        except:
            self.screenShotPage.getScreenShot("Exception occurred while verifying fresh button is displayed")
            assert False

    @allure.step("click on left panel")
    def enter_the_product(self, product):
        self.BasePage = BasePage(self.driver)
        time.sleep(1)
        self.BasePage.enter_text_into_element(self.tbox_globalSearch_xpath, product)
        time.sleep(1)
        self.BasePage.element_click(self.btn_searchSubmit_xpath)
        time.sleep(1)
        self.BasePage.verify_ElementIsDisplayed(self.btn_result_xpath)

    @allure.step("click on account list header")
    def click_on_account_list_header(self):
        self.BasePage = BasePage(self.driver)
        time.sleep(1)
        try:
            if self.BasePage.element_click(self.header_signIn_xpath):
                time.sleep(1)
                self.screenShotPage.getScreenShot("account list button is clicked")
                assert True
            else:
                self.screenShotPage.getScreenShot("account list button is not clicked")
                assert False
        except:
            self.screenShotPage.getScreenShot("Exception occurred while verifying click on account list header")
            assert False
