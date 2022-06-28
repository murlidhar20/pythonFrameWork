from logging import exception

import allure
import pytest
import selenium

from selenium import webdriver
import time

import selenium.common.exceptions

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_locator(self, by_locator):
        return self.driver.find_element(by_locator)

    def get_locators(self, by_locator):
        return self.driver.find_elements(by_locator)

    def element_click(self, by_locator):
        try:
            WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator)).click()
            return True
        except TimeoutException as ex:
            return False
            print(ex.message)

    def element_clear(self, by_locator):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator)).clear()

    def enter_text_into_element(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator)).clear()
            WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator)).send_keys(text)
            return True
        # except exception:
        except selenium.common.exceptions.WebDriverException as e:
            print(" exception: %s" % e, by_locator)
            raise e
            return False

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def verify_element_enable(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def get_page_title(self, title1):
        try:
            WebDriverWait(self.driver, 30).until(ec.title_is(title1))
            return self.driver.title
        except TimeoutException as ex:
            print(ex.message)

    def verify_ElementIsDisplayed(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        return element.is_displayed()

    @allure.step("Capture page title")
    def get_title(self):
        return self.driver.title

    def close_browser(self):
        return self.driver.close()

    def waitFor(self, Time):
        time.sleep(Time)
