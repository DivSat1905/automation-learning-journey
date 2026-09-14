import time
from playwright.sync_api import sync_playwright

def test_register_user():

    email = f"divya{int(time.time())}@test.com"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://automationexercise.com")

        page.get_by_role("link", name="Signup / Login").click()

        page.locator("[data-qa='signup-name']").fill("Divya Test")
        page.locator("[data-qa='signup-email']").fill(email)

        page.locator("[data-qa='signup-button']").click()

        assert page.get_by_text("Enter Account Information").is_visible()

