import allure
import time

from selenium.webdriver.common.by import By

from BasePage.BasePage import BasePage

from utilities.AllureCaptureScreenShot import GetScreenShot


class product_search_page:
    tbox_globalSearch_xpath = (By.XPATH, "//*[@id='twotabsearchtextbox']")
    btn_searchSubmit_xpath = (By.XPATH, "//*[@id='nav-search-submit-button']")
    btn_result_xpath = (By.XPATH, "//*[text()='RESULTS']")
    btn_firstProduct_xpath = (By.XPATH, "(//*[@class='a-link-normal s-no-outline'])[2]")
    txt_addToCartButton_xpath = (By.XPATH, "//input[@id='add-to-cart-button']")
    select_addToCartButton_xpath = (By.CSS_SELECTOR, "//*[@name='dropdown_selected_size_name']")
    txt_productHeader_xpath = (By.XPATH, "//h1[@class='a-size-large a-spacing-none']")
    txt_checkOut_xpath = (By.XPATH, "//*[@id='attach-sidesheet-checkout-button-announce']")
    #txt_checkOut_xpath = (By.XPATH, "//*[@name='proceedToCheckout'][@type='submit']")
    header_productHeader_xpath = (By.XPATH, "//span[@id='nav-cart-count']")
    btn_deleteProduct_xpath = (By.XPATH, "(//*[@data-action='delete'][@data-feature-id='delete'])[1]/span")
    btn_closeButton_xpath = (By.XPATH, "//a[@id='attach-close_sideSheet-link']")



    def __init__(self, driver):
        self.screenShotPage = None
        self.BasePage = None
        self.GetScreenShot = None
        self.driver = driver

    @allure.step("enter the product")
    def enter_the_product(self, product):
        try:
            self.BasePage = BasePage(self.driver)
            self.screenShotPage = GetScreenShot(self.driver)
            if self.BasePage.enter_text_into_element(self.tbox_globalSearch_xpath, product):
                if self.BasePage.element_click(self.btn_searchSubmit_xpath):
                    if self.BasePage.verify_element_is_displayed(self.btn_result_xpath):
                        self.screenShotPage.getScreenShot("result is getting displayed")
                        assert True
                    else:
                        self.screenShotPage.getScreenShot("result is not displayed")
                        assert False
                else:
                    self.screenShotPage.getScreenShot("global search button is not displayed")
                    assert False
            else:
                self.screenShotPage.getScreenShot("global search input box is not displayed")
                assert False
        except:
            self.screenShotPage.getScreenShot("Exception occurred while entering the product ")
            assert False

    @allure.step("click on any brand")
    def click_on_any_brand(self, brand):
        try:
            self.BasePage = BasePage(self.driver)
            self.screenShotPage = GetScreenShot(self.driver)
            brand_name = (
                By.XPATH, "//*[text()='Brand']/../../ul/descendant::span[text()='" + brand + "']/preceding::i[1]")
            print(" brand name : ",brand_name)
            time.sleep(8)
            if self.BasePage.element_click(brand_name):
                time.sleep(8)
                self.screenShotPage.getScreenShot(brand + " brand is selected ")
                assert True
            else:
                self.screenShotPage.getScreenShot(brand + " brand is not selected ")
                assert False
        except:
            self.screenShotPage.getScreenShot("Exception occurred while clicking on any brand")
            assert False

    @allure.step("click on price range")
    def click_on_any_range(self, price_Range):
        try:
            self.BasePage = BasePage(self.driver)
            self.screenShotPage = GetScreenShot(self.driver)
            price_range = (
                By.XPATH, "//span[text()='" + price_Range + "']")
            time.sleep(8)
            if self.BasePage.element_click(price_range):
                time.sleep(8)
                self.screenShotPage.getScreenShot(price_Range + " range is selected ")
                assert True
            else:
                self.screenShotPage.getScreenShot(price_Range + " range is not selected ")
                assert False
        except:
            self.screenShotPage.getScreenShot("Exception occurred while clicking on any price range")
            assert False

    @allure.step("clicked first product")
    def click_on_first_product(self):
        try:
            self.BasePage = BasePage(self.driver)
            if self.BasePage.element_click(self.btn_firstProduct_xpath):
                self.BasePage.switch_to_window(1)
                if self.BasePage.element_click(self.txt_addToCartButton_xpath):
                    if self.BasePage.verify_element_is_displayed(self.txt_checkOut_xpath):
                        self.screenShotPage.getScreenShot("product is added in add to cart")
                        assert True
                    else:
                        self.screenShotPage.getScreenShot("product is not added in add to cart")
                        assert False
                else:
                    self.screenShotPage.getScreenShot("add to cart button is not displayed")
                    assert False
            else:
                self.screenShotPage.getScreenShot("first product is not displayed")
                assert False

        except:
            self.screenShotPage.getScreenShot("Exception occurred while clicking on first product")
            assert False

    @allure.step("delete the project")
    def delete_the_product(self):
        try:
            self.BasePage = BasePage(self.driver)
            self.screenShotPage = GetScreenShot(self.driver)
            if self.BasePage.element_click(self.header_productHeader_xpath):
                time.sleep(8)
                if self.BasePage.element_click(self.btn_deleteProduct_xpath):
                    time.sleep(9)
                    if self.BasePage.verify_element_is_not_displayed(self.btn_deleteProduct_xpath) != 0:
                        self.screenShotPage.getScreenShot("product is deleted")
                        assert True
                    else:
                        self.screenShotPage.getScreenShot("product is not deleted ")
                        assert False
                else:
                    self.screenShotPage.getScreenShot("delete button is not displayed")
                    assert False
            else:
                self.screenShotPage.getScreenShot("product is not added in header")
                assert False

        except:
            self.screenShotPage.getScreenShot("Exception occurred while deleting the product")
            assert False

    @allure.step("clicked on close button on pop-up")
    def click_on_close_button(self):
        try:
            self.BasePage = BasePage(self.driver)
            self.screenShotPage = GetScreenShot(self.driver)
            if self.BasePage.element_click(self.btn_closeButton_xpath):
                time.sleep(20)
                self.screenShotPage.getScreenShot("add to cart is closed ")
                assert True
            else:
                self.screenShotPage.getScreenShot("add to cart is not closed ")
                assert False
        except:
            self.screenShotPage.getScreenShot("Exception occurred while  clicking on close button")
            assert False

