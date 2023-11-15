from selenium.webdriver.common.by import By
from tests.utils.page_object import PageObject


class HomePage(PageObject):
    """
    This class represents the Home Page of the web application.
    It contains methods specifically related to actions and elements on the home page.
    """

    # Element locators
    laptops_category_button_locator = (By.XPATH, '/html/body/div[5]/div/div[1]/div/a[3]')
    macbook_button_locator = (By.XPATH, '//*[@id="tbodyid"]/div[3]/div/div/h4/a')

    # Methods to interact with elements on the page
    def click_laptops_category_button(self) -> None:
        self.click_element(self.laptops_category_button_locator)

    def wait_for_macbook_button(self) -> bool | None:
        return self.wait_for_element_inner_text_to_be(self.macbook_button_locator, 'MacBook air')

    def click_macbook_button(self) -> None:
        self.click_element(self.macbook_button_locator)
