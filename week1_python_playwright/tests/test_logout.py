from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_logout():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")

        login = LoginPage(page)

        login.open_login_page()
        login.login(
            "divyasathish@gmail.com",
            "98765432"
        )
        login.verify_login_success()
        login.logout()

        browser.close()