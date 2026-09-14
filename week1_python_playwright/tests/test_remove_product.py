from playwright.sync_api import sync_playwright, expect


def test_remove_product_from_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://automationexercise.com")

        # Go to Products page
        page.get_by_role("link", name="Products").click()

        # Add first product to cart
        page.locator("a.add-to-cart").first.click()

        # Open cart
        page.get_by_role("link", name="View Cart").click()

        # Verify cart is displayed
        expect(page.locator("#cart_info_table")).to_be_visible()

        # Remove product from cart
        page.locator(".cart_quantity_delete").click()

        # Verify cart is empty
        expect(page.get_by_text("Cart is empty!")).to_be_visible()

        browser.close()