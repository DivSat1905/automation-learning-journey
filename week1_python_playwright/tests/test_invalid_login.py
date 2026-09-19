from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")

        login = LoginPage(page)

        login.open_login_page()
        login.login(
            "invalid@test.com",
            "WrongPassword123"
        )
        login.verify_invalid_login()

        browser.close()