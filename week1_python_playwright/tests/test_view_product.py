from playwright.sync_api import sync_playwright
from pages.products_page import ProductsPage


def test_view_product_details():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")

        products = ProductsPage(page)

        products.open_products()
        products.view_first_product()
        products.verify_product_details_page()

        browser.close()