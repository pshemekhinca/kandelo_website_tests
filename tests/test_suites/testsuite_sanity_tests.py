import unittest
from tests.pages.test_main_page import MainPageTests
from tests.pages.test_home_page import HomePageTests
from tests.pages.test_pages_header_menu import PagesHeaderTests
from tests.pages.test_products_page import ProductsPageTests


def sanity_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(MainPageTests('test_images_number_in_slider'))
    test_suite.addTest(MainPageTests('test_linked_page_title_after_each_main_page_menu_button_click'))
    test_suite.addTest(MainPageTests('test_correct_email_link_href_value'))
    test_suite.addTest(HomePageTests('test_correctly_filled_form_sending'))
    test_suite.addTest(HomePageTests('test_not_filled_form_sending'))
    test_suite.addTest(HomePageTests('test_form_filled_with_wrong_inputs'))
    test_suite.addTest(ProductsPageTests('test_product_blocks_number_equals_products_image_galleries'))
    test_suite.addTest(ProductsPageTests('test_product_weight_information_number_equals_product_blocks_quantity'))
    test_suite.addTest(ProductsPageTests('test_product_dimension_information_number_equals_product_blocks_quantity'))
    test_suite.addTest(PagesHeaderTests('test_correct_page_redirection_after_logo_click'))
    test_suite.addTest(PagesHeaderTests('test_correct_page_redirection_after_menu_button_click'))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(sanity_suite())
