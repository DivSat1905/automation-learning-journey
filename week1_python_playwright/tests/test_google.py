from playwright.sync_api import sync_playwright


def test_launch_homepage():
    with sync_playwright() as p:

        # Launch browser
        browser = p.chromium.launch(headless=False)

        # Open new tab
        page = browser.new_page()

        # Open website
        page.goto("https://automationexercise.com")

        # Verify title
        assert "Automation Exercise" in page.title()

        print("Page Title:", page.title())

        # Close browser
        browser.close()