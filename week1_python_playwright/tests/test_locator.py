from playwright.sync_api import sync_playwright


def test_signup_login_locator():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://automationexercise.com")

        page.get_by_role("link", name="Signup / Login").click()

        assert "login" in page.url

        browser.close()