from .base_test_class import BaseTestClass
from tests.test_data import web_reader
from src.pages import page_factory
from src.utils.wrappers import screenshot
from locators.locators import MainPageLocators


class MainPageTests(BaseTestClass):
    web = web_reader.load()
    main_slider_xpath = MainPageLocators.main_slider_xpath
    en_menu_button_xpath = MainPageLocators.en_menu_button_xpath
    de_menu_button_xpath = MainPageLocators.de_menu_button_xpath
    fr_menu_button_xpath = MainPageLocators.fr_menu_button_xpath
    pl_menu_button_xpath = MainPageLocators.pl_menu_button_xpath
    mail_address_xpath = MainPageLocators.mail_address_xpath

    @screenshot
    def test_main_page_title(self):
        expected_title = "KANDELO - handmade candles"
        self.assert_page_title(self.web['main_url'], expected_title)

    @screenshot
    def test_images_number_in_slider(self):
        expected_images_number = 4
        self.main_page.visit()
        slider_images = self.driver.find_elements_by_xpath(self.main_slider_xpath)
        self.assertEqual(expected_images_number, len(slider_images),
                         f"Required number of images in slider do not match quantity on web {self.web['main_url']}")

    @screenshot
    def test_correct_action_title_after_main_page_ENGLISH_button_click(self):
        expected_text = 'KANDELO - natural handmade candles'
        self.main_page.visit().click_button(self.en_menu_button_xpath)
        self.assert_page_title(self.driver.current_url, expected_text)

    @screenshot
    def test_correct_action_title_after_main_page_DEUTSCH_button_click(self):
        expected_text = 'KANDELO - handgemachte Kerzen'
        self.main_page.visit().click_button(self.de_menu_button_xpath)
        self.assert_page_title(self.driver.current_url, expected_text)

    @screenshot
    def test_correct_action_title_after_main_page_POLSKI_button_click(self):
        expected_text = 'KANDELO - wyjątkowe świece naturalne'
        self.main_page.visit().click_button(self.pl_menu_button_xpath)
        self.assert_page_title(self.driver.current_url, expected_text)

    @screenshot
    def test_correct_email_link_href_value(self):
        expected_text = 'mailto:office@kandelo.eu?subject=contact%20from%20the%20web'
        self.main_page.visit()
        href_value = self.driver.find_element_by_xpath(self.mail_address_xpath).get_attribute('href')
        self.assertEqual(expected_text, href_value, f'Expected email link differ from {href_value}')

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
