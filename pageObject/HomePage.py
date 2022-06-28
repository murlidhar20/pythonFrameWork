import allure
from selenium.webdriver.common.by import By

from BasePage.BasePage import BasePage
import time


class HomePage:
    text_userName_xpath = (By.NAME, "Email")
    text_passWord_xpath = (By.ID, "Password")
    button_login_xpath = (By.XPATH, "//*[text()='Log in']")
    button_MainCustomer = (
        By.XPATH, "(//li[@class='nav-item has-treeview']/descendant::p[contains(text(),'Customers')])[1]")
    button_ChildCustomer = (By.XPATH, "//ul[@class='nav nav-treeview'][@style='display: block;']/li[1]/a/p")

    def __init__(self, driver):
        self.BasePage = None
        self.driver = driver

    @allure.step("click on left panel ")
    def click_on_left_panel(self):
        self.BasePage = BasePage(self.driver)
        time.sleep(1)
        self.BasePage.element_click(self.button_MainCustomer)
        time.sleep(2)
        self.BasePage.element_click(self.button_ChildCustomer)
