import allure
from selenium.webdriver.common.by import By

from BasePage.BasePage import BasePage

import time


class Customer:
    text_userName_xpath = (By.NAME, "Email")
    text_passWord_xpath = (By.ID, "Password")
    button_login_xpath = (By.XPATH, "//*[text()='Log in']")
    input_txt_email = (By.ID, "SearchEmail")
    button_customer = (By.XPATH, "//*[@id='search-customers']")

    button_newCustomer = (By.XPATH, "//*[@class='btn btn-primary'][@href]")
    text_email = (By.ID, "Email")
    text_password = (By.ID, "Password")
    text_firstName = (By.ID, "FirstName")
    text_lastName = (By.ID, "LastName")
    checkBox_Gender = (By.ID, "Gender_Male")
    text_company = (By.ID, "Company")
    text_IsTaxExempt = (By.ID, "IsTaxExempt")
    checkBox_newLetter = (By.CLASS_NAME, "k-input k-readonly")
    text_vendorId = (By.ID, "VendorId")
    text_admitComment = (By.ID, "AdminComment")
    text_successMsg = (By.XPATH, "//*[@class='alert alert-success alert-dismissable']")

    text_save_xpath = (By.NAME, "save")

    def __init__(self, driver):
        self.BasePage = None
        self.driver = driver

    @allure.step("verify exiting customer")
    def verify_existing(self, customerEmail):
        # xpath = "//td[text()='ibNWx@gmail.com']"
        xpath = "//td[text()='" + customerEmail + "']"
        button_customer = (By.XPATH, xpath)
        self.BasePage = BasePage(self.driver)
        self.BasePage.enter_text_into_element(self.input_txt_email, customerEmail)
        time.sleep(2)
        self.BasePage.element_click(self.button_customer)
        time.sleep(2)
        value = self.BasePage.verify_ElementIsDisplayed(button_customer)
        print("value :", value)

    @allure.step("create new customer")
    def created_new_customer(self,emailID,password,firstName,lastName,companyName,message):
        self.BasePage = BasePage(self.driver)

        self.BasePage.element_click(self.button_newCustomer)

        self.BasePage.enter_text_into_element(self.text_email, emailID)
        self.BasePage.enter_text_into_element(self.text_password, password)

        self.BasePage.enter_text_into_element(self.text_firstName, firstName)
        self.BasePage.enter_text_into_element(self.text_lastName, lastName)
        self.BasePage.element_click(self.checkBox_Gender)

        self.BasePage.enter_text_into_element(self.text_company, companyName)
        self.BasePage.element_click(self.text_IsTaxExempt)

        # self.BasePage.enter_text_into_element(self.checkBox_newLetter, "HP letter")

        # self.BasePage.enter_text_into_element(self.text_admitComment, "HP comment")

        self.BasePage.element_click(self.text_save_xpath)

        time.sleep(4)
        msg = self.BasePage.get_element_text(self.text_successMsg)

        time.sleep(8)
        print("last msg : ", msg)
