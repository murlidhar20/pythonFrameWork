from selenium import webdriver
import pytest


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




@pytest.fixture
def setUp(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome('D:\driver\chromedriver_win32\chromedriver.exe')
        driver.maximize_window()
        print("launching chrome driver")

    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="D:\\driver\\geckodriver.exe")
        driver.maximize_window()
        print("launching firefox driver")

    else:
        driver = webdriver.Ie(executable_path="D:\\driver\\IEDriverServer.exe")
        driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")
    
    

