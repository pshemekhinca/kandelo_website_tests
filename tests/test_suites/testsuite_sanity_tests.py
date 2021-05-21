import unittest
from tests.pages.test_main_page import MainPageTests


def sanity_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(MainPageTests('test_images_number_in_slider'))
    test_suite.addTest(MainPageTests('test_linked_page_title_after_each_main_page_menu_button_click'))
    # test_suite.addTest(unittest.makeSuite(PageClass))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(sanity_suite())
