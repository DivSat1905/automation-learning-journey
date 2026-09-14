from playwright.sync_api import sync_playwright, expect


def test_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://automationexercise.com")

        page.get_by_role("link", name="Signup / Login").click()

        page.locator("[data-qa='login-email']").fill(
            "divyasathish@gmail.com"
        )

        page.locator("[data-qa='login-password']").fill(
            "98765432"
        )

        page.locator("[data-qa='login-button']").click()

        expect(
            page.get_by_text("Logged in as")
        ).to_be_visible()

        page.get_by_role("link", name="Logout").click()

        expect(
            page.locator("[data-qa='login-button']")
        ).to_be_visible()

        browser.close()