from tests.test_data import web_reader
from tests.pages.base_test_class import BaseTestClass
from src.utils.wrappers import screenshot
from locators.locators import HeaderLocators


class MainPageTests(BaseTestClass):
    web = web_reader.load()
    logo_xpath = HeaderLocators.logo_xpath
    homepage_button_xpath = HeaderLocators.homepage_button_xpath
    our_candles_button_xpath = HeaderLocators.our_candles_button_xpath
    make_candle_button_xpath = HeaderLocators.make_candle_button_xpath
    where_to_buy_button_xpath = HeaderLocators.where_to_buy_button_xpath
    faq_button_xpath = HeaderLocators.faq_button_xpath
    contact_button_xpath = HeaderLocators.contact_button_xpath

    @screenshot
    def test_correct_page_redirection_after_logo_click(self):
        expected_text = self.web["main_page_title"]
        self.home_page.visit()
        self.click_button(self.logo_xpath)
        self.assert_page_title(self.driver.current_url, expected_text)

    @screenshot
    def test_correct_page_redirection_after_logo_click1(self):
        data = {self.web["en_homepage_title"]: self.homepage_button_xpath,
                self.web["our_candles_title"]: self.our_candles_button_xpath,
                self.web["make_candle_title"]: self.make_candle_button_xpath,
                self.web["where_to_buy_title"]: self.where_to_buy_button_xpath,
                self.web["faq_title"]: self.faq_button_xpath,
                self.web["contact_title"]: self.contact_button_xpath}
        for key, value in data.items():
            with self.subTest(key):
                expected_text = key
                self.home_page.visit()
                self.click_button(value)
                self.assert_page_title(self.driver.current_url, expected_text)
