def launch_application(page):
    page.goto("https://automationexercise.com")

    def login(page, email, password):
        page.get_by_role("link", name="Signup / Login").click()

        page.locator("[data-qa='login-email']").fill(email)
        page.locator("[data-qa='login-password']").fill(password)

        page.locator("[data-qa='login-button']").click()