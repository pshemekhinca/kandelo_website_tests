from tests.pages.base_test_class import BaseTestClass
from tests.test_data import web_reader
from src.utils.wrappers import screenshot
from src.pages.locators import HomePageLocators
from src.pages import page_factory
import time


class HomePageTests(BaseTestClass):
    web = web_reader.load()
    # h1_titles_xpath = HomePageLocators.h1_titles_xpath
    # email_input_xpath = HomePageLocators.email_input_xpath
    # contact_text_field_xpath = HomePageLocators.contact_text_field_xpath
    # send_form_button_xpath = HomePageLocators.send_form_button_xpath
    # error_message_xpath = HomePageLocators.error_message_xpath
    # sent_message_xpath = HomePageLocators.sent_message_xpath

    @screenshot
    def test_number_of_page_sections_with_h1_title(self):
        expected_images_number = 8
        self.home_page.visit()
        page_sections = self.driver.find_elements_by_xpath(self.h1_titles_xpath)
        self.assertEqual(expected_images_number, len(page_sections),
                         f"Required number of page sections does not match quantity on web {self.web['en_homepage_url']}")

    @screenshot
    def test_correctly_filled_form_sending(self):
        self.home_page.visit()
        home_page = page_factory.home_page(self.driver)
        home_page.text_to_input_field(self.email_input_xpath, 'jdoe@oops.op')
        home_page.text_to_input_field(self.contact_text_field_xpath, 'Sample message text')
        self.click_button(self.send_form_button_xpath)

        self.assert_if_element_is_displayed(self.sent_message_xpath)

    @screenshot
    def test_not_filled_form_sending(self):
        self.home_page.visit()
        home_page = page_factory.home_page(self.driver)
        home_page.text_to_input_field(self.email_input_xpath, 'jdoe@oops.op')
        self.click_button(self.send_form_button_xpath)

        self.assert_if_element_is_displayed(self.error_message_xpath)

    @screenshot
    def test_form_filled_with_wrong_inputs(self):
        self.home_page.visit()
        home_page = page_factory.home_page(self.driver)
        home_page.text_to_input_field(self.email_input_xpath, '1234')
        home_page.text_to_input_field(self.contact_text_field_xpath, 'uuuuuuuuuuu')
        self.click_button(self.send_form_button_xpath)

        self.assert_if_element_is_displayed(self.error_message_xpath)
