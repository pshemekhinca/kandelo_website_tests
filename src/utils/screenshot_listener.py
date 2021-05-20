from selenium.webdriver.support.events import AbstractEventListener
from datetime import datetime
import allure
from allure_commons.types import AttachmentType


class ScreenshotListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        # PyCharm debugger cause exception so we need to ignore it
        pycharm_debugger_exceptions = [
            "'WebElement' object has no attribute '__len__'",
            "'WebDriver' object has no attribute '__len__'",
            "'WebDriver' object has no attribute 'shape'",
            "'WebElement' object has no attribute 'shape'"
        ]
        if str(exception) not in pycharm_debugger_exceptions:
            make_screenshot(driver, 'driver')


def make_screenshot(driver, producer):
    screenshot_path = rf"screenshots/{producer}_exception_{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.png"
    driver.get_screenshot_as_file(screenshot_path)
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    print(f"Screenshot saved as {screenshot_path}")