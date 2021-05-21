from tests.test_data import web_reader


class PageFooter:
    def __init__(self, driver):
        web = web_reader.load()
        self.url = web["en_homepage_url"]
        self.driver = driver

    def click_button(self, button_xpath):
        button = self.driver.find_element_by_xpath(button_xpath)
        button.click()
        return self
