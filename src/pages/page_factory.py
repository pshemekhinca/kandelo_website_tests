from src.pages.main_page import MainPage
from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage


def main_page(driver):
    return MainPage(driver)


def home_page(driver):
    return HomePage(driver)


def product_page(driver):
    return ProductPage(driver)
