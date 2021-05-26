from tests.pages.base_test_class import BaseTestClass
from tests.test_data import web_reader
from src.utils.wrappers import screenshot
from src.pages.locators import MainPageLocators


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
    def test_linked_page_title_after_each_main_page_menu_button_click(self):
        data = {self.web['en_homepage_title']: self.en_menu_button_xpath,
                self.web['de_homepage_title']: self.de_menu_button_xpath,
                self.web['pl_homepage_title']: self.pl_menu_button_xpath}
        for key, value in data.items():
            with self.subTest(key):
                expected_text = key
                self.main_page.visit()
                self.click_button(value)
                self.assert_page_title(self.driver.current_url, expected_text)

    @screenshot
    def test_correct_email_link_href_value(self):
        expected_text = 'mailto:office@kandelo.eu?subject=contact%20from%20the%20web'
        self.main_page.visit()
        href_value = self.driver.find_element_by_xpath(self.mail_address_xpath).get_attribute('href')
        self.assertEqual(expected_text, href_value, f'Expected email link differ from {href_value}')
