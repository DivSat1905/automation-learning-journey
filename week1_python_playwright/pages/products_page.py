from playwright.sync_api import expect


class ProductsPage:

    def __init__(self, page):
        self.page = page

    def open_products(self):
        self.page.locator("a[href='/products']").click()

    def add_first_product_to_cart(self):
        self.page.locator(".product-image-wrapper").first.hover()
        self.page.locator(".add-to-cart").first.click()

        expect(self.page.locator("#cartModal")).to_be_visible()
        self.page.get_by_text("Continue Shopping").click()

    def search_product(self, product_name):
        self.page.fill("#search_product", product_name)
        self.page.click("#submit_search")

    def verify_search_result(self):
        expect(
            self.page.get_by_text("Blue Top").first
        ).to_be_visible()

    def view_first_product(self):
        self.page.locator("a[href*='/product_details/']").first.click()

    def verify_product_details_page(self):
        assert "/product_details/" in self.page.url