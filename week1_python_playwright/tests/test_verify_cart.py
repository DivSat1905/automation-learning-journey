from playwright.sync_api import sync_playwright
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_verify_cart_contents():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")

        products = ProductsPage(page)
        cart = CartPage(page)

        products.open_products()
        products.add_first_product_to_cart()

        cart.open_cart()
        cart.verify_cart()

        browser.close()