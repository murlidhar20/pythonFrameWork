from logging import exception

import allure
import pytest
import selenium

from selenium import webdriver
import time

import selenium.common.exceptions

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_locator(self, by_locator):
        return self.driver.find_element(by_locator)

    def get_locators(self, by_locator):
        return self.driver.find_elements(by_locator)

    def element_click(self, by_locator):
        try:
            WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located(by_locator)).click()
            return True
        except TimeoutException as ex:
            return False
            print(ex.message)

    def element_clear(self, by_locator):
        WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located(by_locator)).clear()

    def enter_text_into_element(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located(by_locator)).clear()
            WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located(by_locator)).send_keys(text)
            return True
        # except exception:
        except selenium.common.exceptions.WebDriverException as e:
            print(" exception: %s" % e, by_locator)
            raise e
            return False

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def verify_element_enable(self, by_locator):
        element = WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def get_page_title(self, title1):
        try:
            WebDriverWait(self.driver, 120).until(ec.title_is(title1))
            return self.driver.title
        except TimeoutException as ex:
            print(ex.message)

    @allure.step("Capture page title")
    def get_title(self):
        return self.driver.title

    # def close_browser(self):
    #     return self.driver.close()

    def waitFor(self, Time):
        time.sleep(Time)

    def get_locators1(self, by_locator_type):
        return self.driver.find_elements(by_locator_type)

    def get_locators2(self):
        return self.driver.find_elements(By.XPATH, "//*[@id='nav-xshop']/a[text()='Fresh']")

    def get_locators3(self, xpath):
        return self.driver.find_elements(xpath)

    def selectByVisibleText(self, by_locator, value):

        # select = Select(WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(by_locator)))
        # print(" ====",select.options)
        # select.select_by_index(2)

        select = Select(self.driver.find_element_by_xpath("//*[@id='native_dropdown_selected_size_name']"))

        # select by visible text
        # select.select_by_visible_text('Banana')

        # select by value
        select.select_by_value('1')

    def verify_element_is_not_displayed(self, by_locator):
        try:
            element = self.driver.find_element(By.XPATH,
                                               "(//*[@data-action='delete'][@data-feature-id='delete'])[1]/span")
            return element.size
        except TimeoutException as ex:
            print(ex.message)
            raise ex
            return element.size

    def find_element(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located(by_locator))
            return element
        except TimeoutException as ex:
            print(ex.message)
            raise ex
            return False

    def mouse_hover(self, by_locator):
        try:
            a = ActionChains(self.driver)
            element = WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located(by_locator))
            a.move_to_element(element).perform()
            return True
        except TimeoutException as ex:
            print(ex.message)
            raise ex
            return False

    def find_elements(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 120).until(ec.presence_of_all_elements_located(by_locator))
            return element
        except TimeoutException as ex:
            print(ex.message)
            raise ex
            return False

    #####################################################################

    def back(self):
        try:
            return self.driver.back()
        except TimeoutException as ex:
            print(ex.message)
            raise ex
            return False

    def close_browser(self):
        try:
            return self.driver.close()
        except TimeoutException as ex:
            print(ex.message)
            raise ex
            return False

    def verify_element_is_displayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 120).until(ec.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except TimeoutException as ex:
            print(ex.message)
            raise ex
            return False

    def switch_to_window(self, index):
        try:
            return self.driver.switch_to.window(self.driver.window_handles[index])
        except TimeoutException as ex:
            print(ex.message)
            raise ex
            return False

    def implicitly_waits(self, timeunit):
        try:
            return self.driver.implicitly_wait(timeunit)
        except TimeoutException as ex:
            print(ex.message)
            raise ex
            return False
