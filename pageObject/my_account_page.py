import allure
import time

from selenium.webdriver.common.by import By

from BasePage.BasePage import BasePage

from utilities.AllureCaptureScreenShot import GetScreenShot


class my_account_page:
    header_amazonPayBalance_xpath = (By.XPATH, "//h2[contains(text(),'Amazon Pay balance')]")
    ele_amazonPayBalance_xpath = (
        By.XPATH, "//span[contains(text(),'Gift & Credits balance:')]/../span[contains(text(),'₹')]")
    btn_continue_xpath = (By.XPATH, "//*[@id='form-submit-button']")
    btn_selectPaymentMethod_xpath = (By.XPATH, "//h1[text()='Select a payment method']")
    tbox_enterAmount_xpath = (By.XPATH, "//input[@placeholder='₹ Enter an amount...']")
    btn_yourAddress_xpath = (By.XPATH, "//h2[contains(text(), ' Your Addresses')]")
    btn_yourAddressEdit_xpath = (By.XPATH, "(//*[contains(text(),'Edit')])[1]")

    def __init__(self, driver):
        self.screenShotPage = None
        self.BasePage = None
        self.GetScreenShot = None
        self.driver = driver

    @allure.step("view amazon pay balance")
    def view_amazon_pay_balance(self):
        self.BasePage = BasePage(self.driver)
        self.screenShotPage = GetScreenShot(self.driver)
        time.sleep(1)
        try:
            if self.BasePage.element_click(self.header_amazonPayBalance_xpath):
                pay_balance = self.BasePage.get_element_text(self.ele_amazonPayBalance_xpath)
                rupees = "₹"
                if rupees in pay_balance:
                    self.screenShotPage.getScreenShot(pay_balance + " is captured")
                    assert True
                else:
                    self.screenShotPage.getScreenShot(pay_balance + " not is captured")
                    assert False
            else:
                self.screenShotPage.getScreenShot("amazon pay balance is not displayed")
                assert False
        except:
            self.screenShotPage.getScreenShot("Exception occurred while viewing amazon pay balance")
            assert False

    @allure.step("add money")
    def add_money(self, amount):
        try:
            self.BasePage = BasePage(self.driver)
            self.screenShotPage = GetScreenShot(self.driver)
            if self.BasePage.enter_text_into_element(self.tbox_enterAmount_xpath, amount):
                if self.BasePage.element_click(self.btn_continue_xpath):
                    if self.BasePage.verify_element_is_displayed(self.btn_selectPaymentMethod_xpath):
                        self.screenShotPage.getScreenShot("user is able to navigate to Select a payment method page")
                        assert True
                    else:
                        self.screenShotPage.getScreenShot("select payment method is not displayed")
                        assert False
                else:
                    self.screenShotPage.getScreenShot(" continue button is not displayed")
                    assert False
            else:
                self.screenShotPage.getScreenShot(amount + " amount is not displayed")
                assert False
        except:
            self.screenShotPage.getScreenShot("Exception occurred adding the money")
            assert False

    @allure.step("click on address and verify edit button")
    def click_on_address_and_verify_edit_button(self):
        try:
            self.BasePage = BasePage(self.driver)
            self.screenShotPage = GetScreenShot(self.driver)
            print("click on your address ")
            if self.BasePage.element_click(self.btn_yourAddress_xpath):
                print("click on your address 2 ")
                time.sleep(45)
                if self.BasePage.verify_element_is_displayed(self.btn_yourAddressEdit_xpath):
                    print("click on your address 3 ")
                    self.screenShotPage.getScreenShot("edit button on address is displayed")
                    assert True
                else:
                    self.screenShotPage.getScreenShot("edit button on address is not displayed")
                    assert False
            else:
                    self.screenShotPage.getScreenShot("address button is not displayed")
                    assert False
        except:
            self.screenShotPage.getScreenShot("Exception occurred while clicking on address and verify edit button")
            assert False



