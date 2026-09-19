from playwright.sync_api import expect

class LoginPage:

    def __init__(self, page):
        self.page = page

    def open_login_page(self):
        self.page.get_by_role(
            "link",
            name="Signup / Login"
        ).click()

    def login(self, email, password):

        self.page.locator(
            "[data-qa='login-email']"
        ).fill(email)

        self.page.locator(
            "[data-qa='login-password']"
        ).fill(password)

        self.page.locator(
            "[data-qa='login-button']"
        ).click()

    def verify_login_success(self):

        expect(
            self.page.get_by_text("Logged in as")
        ).to_be_visible()

    def verify_invalid_login(self):

        expect(
            self.page.get_by_text(
                "Your email or password is incorrect!"
            )
        ).to_be_visible()

    def logout(self):

        self.page.get_by_role(
            "link",
            name="Logout"
        ).click()