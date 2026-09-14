from playwright.sync_api import sync_playwright


def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://automationexercise.com")

        # Click Signup / Login
        page.get_by_role("link", name="Signup / Login").click()

        # Enter invalid credentials
        page.locator("[data-qa='login-email']").fill(
            "invalid@test.com"
        )

        page.locator("[data-qa='login-password']").fill(
            "WrongPassword123"
        )

        # Click Login
        page.locator("[data-qa='login-button']").click()

        # Verify error message
        assert page.get_by_text(
            "Your email or password is incorrect!"
        ).is_visible()

        browser.close()