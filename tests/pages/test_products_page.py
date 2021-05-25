from tests.pages.base_test_class import BaseTestClass
from tests.test_data import web_reader
from src.utils.wrappers import screenshot
from src.pages.locators import ProductsPageLocators


class ProductsPageTests(BaseTestClass):
    web = web_reader.load()
    products_titles_xpath = ProductsPageLocators.products_titles_xpath
    top_products_list_xpath = ProductsPageLocators.top_products_list_xpath
    products_gallery_xpath = ProductsPageLocators.products_gallery_xpath
    weight_field_xpath = ProductsPageLocators.weight_field_xpath
    dimensions_field_xpath = ProductsPageLocators.dimensions_field_xpath

    @screenshot
    def test_top_products_list_number_equals_titled_products_description_blocks(self):
        self.products_page.visit()
        top_products_list = self.driver.find_elements_by_xpath(self.top_products_list_xpath)
        titled_products_blocks = self.driver.find_elements_by_xpath(self.products_titles_xpath)
        # top_products_list minus 4 elements in the group (additional 2 lines and 2 section titles)
        self.assertEqual(len(top_products_list) - 4, len(titled_products_blocks),
                         f"Number of product blocks differ from top product links quantity on page {self.web['en_products_url']}")

    @screenshot
    def test_product_blocks_number_equals_products_image_galleries(self):
        self.products_page.visit()
        products_blocks = self.driver.find_elements_by_xpath(self.products_titles_xpath)
        galleries_list = self.driver.find_elements_by_xpath(self.products_gallery_xpath)

        self.assertEqual(len(products_blocks), len(galleries_list),
                         f"Required number of page sections does not match product galleries quantity on web {self.web['en_products_url']}")

    @screenshot
    def test_product_weight_information_number_equals_product_blocks_quantity(self):
        self.products_page.visit()
        products_blocks = self.driver.find_elements_by_xpath(self.products_titles_xpath)
        product_weight_information = self.driver.find_elements_by_xpath(self.weight_field_xpath)

        self.assertEqual(len(products_blocks), len(product_weight_information),
                         f"Products blocks number not equals weight information occurances on web {self.web['en_products_url']}")


    @screenshot
    def test_product_dimension_information_number_equals_product_blocks_quantity(self):
        self.products_page.visit()
        products_blocks = self.driver.find_elements_by_xpath(self.products_titles_xpath)
        product_dimensions_information = self.driver.find_elements_by_xpath(self.dimensions_field_xpath)
        # products_blocks minus 1 element in the group (one product doesn't have dimensions info)
        self.assertEqual(len(products_blocks)-1, len(product_dimensions_information),
                         f"Products blocks number not equals dimensions information occurances on web {self.web['en_products_url']}")

