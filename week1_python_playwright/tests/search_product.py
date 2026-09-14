from playwright.sync_api import sync_playwright, expect


def test_search_product():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://automationexercise.com")

        # Click Products
        page.get_by_role("link", name="Products").click()

        # Verify Products page is displayed
        assert "products" in page.url.lower()

        # Search for a product
        page.locator("#search_product").fill("Blue Top")

        page.locator("#submit_search").click()

        # Verify searched product is visible
        expect(page.get_by_text("Blue Top").first).to_be_visible()

        # View product details
        page.get_by_role("link", name="View Product").first.click()

        # Verify product details section
        expect(page.locator(".product-information")).to_be_visible()

        browser.close()