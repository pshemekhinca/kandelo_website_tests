from tests.test_data import web_reader
from src.pages import page_factory


class ProductsPage:
    def __init__(self, driver):
        web = web_reader.load()
        self.url = web["en_products_url"]
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        return self


