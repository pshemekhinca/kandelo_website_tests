from src.utils.screenshot_listener import make_screenshot
from selenium.common.exceptions import TimeoutException


def screenshot(test_fun):
    def wrapper(self):
        try:
            return test_fun(self)
        except AssertionError as ex:
            make_screenshot(self.driver, 'assert')
            raise ex
        except TimeoutException as ex:
            make_screenshot(self.driver, 'timeout')
            raise ex

    return wrapper
