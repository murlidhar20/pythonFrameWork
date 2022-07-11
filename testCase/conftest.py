from selenium import webdriver
import pytest

import os

"""
@pytest.fixture
def setUp():
    driver = webdriver.Chrome('D:\driver\chromedriver_win32\chromedriver.exe')
    driver.maximize_window()
    return driver
    
    """

'''

@pytest.fixture
def setUp():
    #driver = webdriver.Chrome('D:\driver\chromedriver_win32\chromedriver.exe')
    driver = webdriver.Firefox(executable_path="D:\\driver\\geckodriver.exe")
    driver.maximize_window()
    return driver
    
    '''

'''
@pytest.fixture
def setUp():
    # driver = webdriver.Chrome('D:\driver\chromedriver_win32\chromedriver.exe')
    driver = webdriver.Ie(executable_path="D:\\driver\\IEDriverServer.exe")
    driver.maximize_window()
    return driver
    
    '''

# @pytest.fixture
# def setUp(browser):
#     if browser == 'chrome':
#         #driver = webdriver.Chrome('D:\driver\chromedriver_win32\chromedriver.exe')
#         # D:\driver\driver_version\chromedriver_win32 (1)\chromedriver.exe
#
#         driver = webdriver.Chrome('D:\driver\driver_version\chromedriver_win32 (1)\chromedriver.exe')
#         driver.maximize_window()
#         print("launching chrome driver")
#
#     elif browser == 'firefox':
#         driver = webdriver.Firefox(executable_path="D:\\driver\\geckodriver.exe")
#         driver.maximize_window()
#         print("launching firefox driver")
#
#     else:
#         driver = webdriver.Ie(executable_path="D:\\driver\\IEDriverServer.exe")
#         driver.maximize_window()
#     return driver
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture
# def browser(request):
#     return request.config.getoption("--browser")


########### pytest HTML Report ################


'''
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    
    '''


@pytest.fixture
def setUp(browser):
    if browser == 'chrome':
        parent_dir = os.getcwd()
        directory = '\\configuration\\chromedriver.exe'
        path = parent_dir + directory
        driver = webdriver.Chrome(path)
        driver.maximize_window()
        print("launching chrome driver")

    elif browser == 'firefox':
        parent_dir = os.getcwd()
        directory = '\\configuration\\geckodriver.exe'
        path = parent_dir + directory
        driver = webdriver.Firefox(executable_path=path)
        driver.maximize_window()
        print("launching firefox driver")

    else:

        parent_dir = os.getcwd()
        directory = '\\configuration\\IEDriverServer.exe'
        path = parent_dir + directory
        driver = webdriver.Ie(executable_path=path)
        driver.maximize_window()
        print("launching IE driver")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")
