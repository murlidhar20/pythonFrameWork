import allure
from allure_commons.types import AttachmentType


class GetScreenShot:

    def __init__(self, driver):
        self.driver = driver

    def getScreenShot(self, description):
        allure.attach(self.driver.get_screenshot_as_png(), name=description,
                      attachment_type=AttachmentType.PNG)
