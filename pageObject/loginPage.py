import allure
import time

from selenium.webdriver.common.by import By

from BasePage.BasePage import BasePage


class LoginPage:
    text_userName_xpath = (By.NAME, "Email")
    text_passWord_xpath = (By.ID, "Password")
    button_login_xpath = (By.XPATH, "//*[text()='Log in']")

    def __init__(self, driver):
        self.BasePage = None
        self.driver = driver

    @allure.step("enter userName and password and click on login button")
    def loginPage(self, userName, password):
        self.BasePage = BasePage(self.driver)
        self.BasePage.enter_text_into_element(self.text_userName_xpath, userName)
        self.BasePage.enter_text_into_element(self.text_passWord_xpath, password)
        time.sleep(1)
        self.BasePage.element_click(self.button_login_xpath)
        time.sleep(1)
        self.BasePage.get_page_title("Dashboard / nopCommerce administration")
