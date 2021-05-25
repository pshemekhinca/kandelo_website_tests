from tests.test_data import web_reader


class HomePage:
    def __init__(self, driver):
        web = web_reader.load()
        self.url = web['en_homepage_url']
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        return self

    def text_to_input_field(self, input_field_xpath, input_text):
        """Fill selected input field with given text
        :param input_field_xpath: given input field xpath
        :param input_text: text to fill with
        :return: None
        """
        input_field = self.driver.find_element_by_xpath(input_field_xpath)
        input_field.send_keys(input_text)
        return self









