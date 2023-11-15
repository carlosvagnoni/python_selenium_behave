from selenium.webdriver.common.by import By
from tests.utils.page_object import PageObject


class CartPage(PageObject):
    """
    This class represents the Cart Page of the web application.
    It contains methods specifically related to the cart functionality.
    """

    # Element locators
    macbook_title_in_cart_locator = (By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')

    # Methods to interact with elements on the page
    def wait_for_macbook_title_in_cart(self) -> bool | None:
        self.wait_for_element_presence(self.macbook_title_in_cart_locator)
        return self.wait_for_element_inner_text_to_be(self.macbook_title_in_cart_locator, 'MacBook air')

    def verify_macbook_title_in_cart(self, expect_text: str) -> None:
        self.verify_element_text(self.macbook_title_in_cart_locator, expect_text)
