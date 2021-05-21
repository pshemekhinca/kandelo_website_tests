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

    def get_page_title(self, url):
        """WebDriver gets webpage title of given url
        :param url: given url
        :return: webpage title text
        """
        self.driver.get(url)
        return self.driver.title

    def assert_page_title(self, url, expected_title):
        """Method for title page test
        :param url: given url
        :param expected_title: expected webpage title according to documentation
        :return: None
        """
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title,
                         f'Expected title differ from actual on page: {url}')