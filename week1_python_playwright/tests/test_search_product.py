from playwright.sync_api import sync_playwright
from pages.products_page import ProductsPage


def test_search_product():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")

        products = ProductsPage(page)

        products.open_products()
        products.search_product("Blue Top")
        products.verify_search_result()

        browser.close()