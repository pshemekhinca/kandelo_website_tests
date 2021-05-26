import unittest
from tests.pages.test_main_page import MainPageTests
from tests.pages.test_home_page import HomePageTests
from tests.pages.test_products_page import ProductsPageTests


def all_kandelo_tests_suite():
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.makeSuite(MainPageTests))
    test_suite.addTest(unittest.makeSuite(HomePageTests))
    test_suite.addTest(unittest.makeSuite(ProductsPageTests))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(all_kandelo_tests_suite())
