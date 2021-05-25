from src.pages.main_page import MainPage
from src.pages.home_page import HomePage
from src.pages.products_page import ProductsPage


def main_page(driver):
    return MainPage(driver)


def home_page(driver):
    return HomePage(driver)


def products_page(driver):
    return ProductsPage(driver)
