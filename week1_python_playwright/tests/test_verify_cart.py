from playwright.sync_api import sync_playwright, expect


def test_verify_cart_contents():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://automationexercise.com")

        # Navigate to Products
        page.get_by_role("link", name="Products").click()

        # Add first product to cart
        page.locator("a.add-to-cart").first.click()

        # Open Cart
        page.get_by_role("link", name="View Cart").click()

        # Verify cart table is displayed
        expect(page.locator("#cart_info_table")).to_be_visible()

        # Verify product name
        expect(page.get_by_text("Blue Top")).to_be_visible()

        # Verify quantity
        expect(page.locator(".cart_quantity")).to_contain_text("1")

        # Verify price
        expect(page.locator(".cart_price")).to_be_visible()

        # Verify total
        expect(page.locator(".cart_total")).to_be_visible()

        browser.close()