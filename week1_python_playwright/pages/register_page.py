from playwright.sync_api import expect

class RegisterPage:

    def __init__(self,page):
        self.page = page

    def open_signup(self):

        self.page.get_by_role(
            "link",
            name="Signup / Login"
        ).click()

    def register(self,name,email):

        self.page.locator(
            "[data-qa='signup-name']"
        ).fill(name)

        self.page.locator(
            "[data-qa='signup-email']"
        ).fill(email)

        self.page.locator(
            "[data-qa='signup-button']"
        ).click()

    def verify_account_created(self):

        expect(
            self.page.get_by_text(
                "Enter Account Information"
            )
        ).to_be_visible()