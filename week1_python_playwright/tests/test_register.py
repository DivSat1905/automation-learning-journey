import time
from playwright.sync_api import sync_playwright
from pages.register_page import RegisterPage

def test_register_user():

    email = f"divya{int(time.time())}@test.com"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")

        register = RegisterPage(page)

        register.open_signup()
        register.register(
            "Divya Test",
            email
        )
        register.verify_account_created()

        browser.close()