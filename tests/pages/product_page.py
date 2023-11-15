from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from tests.utils.page_object import PageObject


class ProductPage(PageObject):
    """
    This class represents the Product Page of the web application.
    It contains methods specifically related to product details and actions.
    """

    # Element locators
    macbook_title_locator = (By.XPATH, '//*[@id="tbodyid"]/h2')
    add_to_cart_button_locator = (By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')

    # Methods to interact with elements on the page
    def wait_for_macbook_title(self) -> WebElement | None:
        return self.wait_for_element_presence(self.macbook_title_locator)

    def click_add_to_cart(self) -> None:
        self.click_element(self.add_to_cart_button_locator)
        self.wait_for_seconds(1)

    def verify_alert_successful_added_to_cart(self, expected_text) -> None:
        self.verify_alert_text(expected_text)
