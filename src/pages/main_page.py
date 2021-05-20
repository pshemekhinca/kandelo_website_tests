from tests.test_data import web_reader


class MainPage:
    def __init__(self, driver):
        web = web_reader.load()
        self.url = web['main_url']
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        return self

    def click_button(self, button_xpath):
        button = self.driver.find_element_by_xpath(button_xpath)
        button.click()
        return self


