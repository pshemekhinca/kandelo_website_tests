import unittest
from tests.pages.test_main_page import MainPageTests
from tests.pages.test_home_page import HomePageTests


def smoke_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(MainPageTests('test_main_page_title'))
    test_suite.addTest(HomePageTests('test_number_of_home_page_sections_with_h1_title'))
    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
runner.run(smoke_suite())
