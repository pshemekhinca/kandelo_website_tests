from tests.test_data import web_reader


class MainPage:
    def __init__(self, driver):
        web = web_reader.load()
        self.url = web['main_url']
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        return self




