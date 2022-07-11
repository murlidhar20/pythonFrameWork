import allure
import time

from selenium.webdriver.common.by import By

from BasePage.BasePage import BasePage

from utilities.AllureCaptureScreenShot import GetScreenShot
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage:
    '''

    text_userName_xpath = (By.NAME, "Email")
    text_passWord_xpath = (By.ID, "Password")
    button_login_xpath = (By.XPATH, "//*[text()='Log in']")

     '''

    text_userName_id = (By.ID, "ap_email")
    text_continue_id = (By.ID, "continue")
    text_passWord_id = (By.ID, "ap_password")
    button_login_xpath = (By.XPATH, "//*[@id='signInSubmit']")
    button_signIn_xpath = (By.XPATH, "//*[text()='Hello, Sign in']")
    header_signIn_xpath = (By.XPATH, "//*[@class='nav-line-1-container']")

    btn_signOut_xpath = (By.XPATH, "//*[text()='Sign Out']")

    def __init__(self, driver):
        self.screenShotPage = None
        self.BasePage = None
        self.GetScreenShot = None
        self.driver = driver

    # @allure.step("enter userName and password and click on login button")
    # def login_page(self, userName, password, expectedPageTitle):
    #     self.BasePage = BasePage(self.driver)
    #     self.screenShotPage = GetScreenShot(self.driver)
    #     self.BasePage.enter_text_into_element(self.text_userName_xpath, userName)
    #     self.BasePage.enter_text_into_element(self.text_passWord_xpath, password)
    #     time.sleep(1)
    #     self.BasePage.element_click(self.button_login_xpath)
    #     time.sleep(4)
    #     actualPageTitle = self.BasePage.get_page_title("Dashboard / nopCommerce administration")
    #     time.sleep(4)
    #     if actualPageTitle == expectedPageTitle:
    #         self.screenShotPage.getScreenShot("user is navigated to Home page")
    #         assert True
    #     else:
    #         self.screenShotPage.getScreenShot("user is not navigated to Home page")
    #         assert False

    '''

    @allure.step("enter userName and password and click on login button")
    def login_to_application(self, userName, password):

        try:
            self.BasePage = BasePage(self.driver)
            self.screenShotPage = GetScreenShot(self.driver)
            self.BasePage.waitFor(3)
            self.BasePage.element_click(self.button_signIn_xpath)
            self.BasePage.waitFor(2)
            self.BasePage.enter_text_into_element(self.text_userName_id, userName)
            self.BasePage.waitFor(1)
            self.BasePage.element_click(self.text_continue_id)
            self.BasePage.waitFor(2)
            self.BasePage.enter_text_into_element(self.text_passWord_id, password)
            self.BasePage.waitFor(1)
            self.BasePage.element_click(self.button_login_xpath)
            self.BasePage.waitFor(4)
            actualPageTitle = self.BasePage.getTitle()
            print("actualPageTitle :", actualPageTitle)
            if actualPageTitle == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in":
                self.screenShotPage.getScreenShot("user is navigated to Home page")
                assert True
            else:
                self.screenShotPage.getScreenShot("user is not navigated to Home page")
                assert False
        except:
            self.screenShotPage.getScreenShot("Exception occurred while the login the application")
            assert False
        
        '''

    @allure.step("enter userName and password and click on login button")
    def login_to_application(self, userName, password):
        try:
            self.BasePage = BasePage(self.driver)
            self.screenShotPage = GetScreenShot(self.driver)
            self.BasePage.verify_element_is_displayed(self.button_signIn_xpath)
            if self.BasePage.element_click(self.button_signIn_xpath):
                if self.BasePage.enter_text_into_element(self.text_userName_id, userName):
                    if self.BasePage.element_click(self.text_continue_id):
                        if self.BasePage.enter_text_into_element(self.text_passWord_id, password):
                            if self.BasePage.element_click(self.button_login_xpath):
                                time.sleep(45)
                                actualPageTitle = self.BasePage.get_title()
                                if len(actualPageTitle):
                                    if actualPageTitle == "Online Shopping site in India: Shop Online for Mobiles, " \
                                                          "Books, Watches, Shoes and More - Amazon.in":
                                        self.screenShotPage.getScreenShot("user is navigated to Home page")
                                        assert True
                                    else:
                                        self.screenShotPage.getScreenShot("user is not navigated to Home page")
                                        assert False
                                else:
                                    self.screenShotPage.getScreenShot("Unable to capture Page title")
                                    assert False
                            else:
                                self.screenShotPage.getScreenShot("Unable to sign in page")
                                assert False
                        else:
                            self.screenShotPage.getScreenShot("Unable to entered password name")
                            assert False
                    else:
                        self.screenShotPage.getScreenShot("Unable to clicked continue button in login page")
                        assert False
                else:
                    self.screenShotPage.getScreenShot("Unable to entered user name")
                    assert False
            else:
                self.screenShotPage.getScreenShot("Unable to clicked on Sign in")
                assert False
        except:
            self.screenShotPage.getScreenShot("Exception occurred while the login the application")
            assert False

    @allure.step("user is able to logout")
    def log_out(self):
        try:
            self.BasePage = BasePage(self.driver)
            self.screenShotPage = GetScreenShot(self.driver)
            if self.BasePage.mouse_hover(self.header_signIn_xpath):
                if self.BasePage.element_click(self.btn_signOut_xpath):
                    assert True
                    self.screenShotPage.getScreenShot("user is able to logout")
                else:
                    self.screenShotPage.getScreenShot("logout button is not displayed")
                    assert False
            else:
                self.screenShotPage.getScreenShot("sign in button is not displayed")
                assert False
        except:
            self.screenShotPage.getScreenShot("Exception occurred while the logout the application")
            assert False
