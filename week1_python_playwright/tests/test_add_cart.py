from playwright.sync_api import sync_playwright, expect


def test_add_product_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://automationexercise.com")

        page.get_by_role("link", name="Products").click()

        # Hover over first product
        first_product = page.locator(".product-image-wrapper").first
        first_product.hover()

        # Add to cart
        page.locator("a.add-to-cart").first.click()

        # Open cart
        page.get_by_role("link", name="View Cart").click()

        expect(page.locator("#cart_info_table")).to_be_visible()

        browser.close()