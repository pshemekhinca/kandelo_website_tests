import unittest
from selenium import webdriver
from configuration import config_reader
from src.pages import page_factory


class BaseTestClass(unittest.TestCase):
    def setUp(self):
        config = config_reader.load()
        self.driver = webdriver.Chrome(executable_path=config['chromedriver_path'])
        self.driver.maximize_window()
        self.main_page = page_factory.main_page(self.driver)

    def tearDown(self):
        self.driver.quit()
