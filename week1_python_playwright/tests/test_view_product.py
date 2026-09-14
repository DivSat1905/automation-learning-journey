from playwright.sync_api import sync_playwright, expect


def test_view_product_details():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://automationexercise.com")

        # Click Products
        page.get_by_role("link", name="Products").click()

        # Click first View Product link
        page.locator("a[href*='/product_details/']").first.click()

        # Verify product details page is displayed
        expect(page.locator(".product-information")).to_be_visible()

        # Verify product information
        expect(page.locator(".product-information")).to_contain_text("Category")
        expect(page.locator(".product-information")).to_contain_text("Availability")
        expect(page.locator(".product-information")).to_contain_text("Condition")
        expect(page.locator(".product-information")).to_contain_text("Brand")

        browser.close()