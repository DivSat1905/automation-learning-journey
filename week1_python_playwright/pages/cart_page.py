from playwright.sync_api import expect


class CartPage:

    def __init__(self, page):
        self.page = page

    def open_cart(self):
        self.page.locator("a[href='/view_cart']").first.click()

    def verify_cart(self):
        expect(
            self.page.locator("#cart_info")
        ).to_be_visible()

    def remove_product(self):
        self.page.locator(".cart_quantity_delete").click()

    def verify_cart_empty(self):
        expect(
            self.page.get_by_text("Cart is empty!")
        ).to_be_visible()