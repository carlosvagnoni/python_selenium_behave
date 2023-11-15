from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from tests.utils.page_object import PageObject


class BasePage(PageObject):
    """
    This class represents the header and footer for the web application.
    It contains methods to interact with common elements like signup, login, and shopping cart.
    """

    # Element locators
    signup_button_locator = (By.XPATH, '//*[@id="signin2"]')
    signup_title_locator = (By.XPATH, '//*[@id="signInModalLabel"]')
    login_button_locator = (By.XPATH, '//*[@id="login2"]')
    login_title_locator = (By.XPATH, '//*[@id="logInModalLabel"]')
    login_username_input_locator = (By.XPATH, '//*[@id="loginusername"]')
    login_password_input_locator = (By.XPATH, '//*[@id="loginpassword"]')
    signup_username_input_locator = (By.XPATH, '//*[@id="sign-username"]')
    signup_password_input_locator = (By.XPATH, '//*[@id="sign-password"]')
    submit_signup_button_locator = (By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')
    submit_login_button_locator = (By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    logged_in_username_locator = (By.XPATH, '//*[@id="nameofuser"]')
    cart_button_locator = (By.XPATH, '//*[@id="cartur"]')

    # Methods to interact with elements on the page
    def click_signup_button(self) -> None:
        self.click_element(self.signup_button_locator)

    def wait_for_signup_title(self) -> WebElement | None:
        return self.wait_for_element_visibility(self.signup_title_locator)

    def verify_signup_title(self) -> None:
        self.verify_element_text(self.signup_title_locator, 'Sign up')

    def click_login_button(self) -> None:
        self.click_element(self.login_button_locator)

    def wait_for_login_title(self) -> WebElement | None:
        return self.wait_for_element_visibility(self.login_title_locator)

    def verify_login_title(self) -> None:
        self.verify_element_text(self.login_title_locator, 'Log in')

    def enter_login_username(self, input_value: str) -> None:
        self.enter_text(self.login_username_input_locator, input_value)

    def enter_login_password(self, input_value: str) -> None:
        self.enter_text(self.login_password_input_locator, input_value)

    def enter_signup_username(self, input_value: str) -> None:
        self.enter_text(self.signup_username_input_locator, input_value)

    def enter_signup_password(self, input_value: str) -> None:
        self.enter_text(self.signup_password_input_locator, input_value)

    def verify_entered_credentials(self, username: str, password: str) -> None:
        self.verify_element_text_value(self.signup_username_input_locator, username)
        self.verify_element_text_value(self.signup_password_input_locator, password)

    def submit_signup(self) -> None:
        self.click_element(self.submit_signup_button_locator)
        self.wait_for_seconds(1)

    def verify_alert_successful_signup(self, expected_text) -> None:
        self.verify_alert_text(expected_text)

    def submit_login(self) -> None:
        self.click_element(self.submit_login_button_locator)

    def wait_for_logged_in_username(self, text) -> bool | None:
        self.wait_for_element_to_disappear(self.login_title_locator)
        return self.wait_for_element_inner_text_to_be(self.logged_in_username_locator, text)

    def verify_logged_in_username(self, expect_text: str) -> None:
        self.verify_element_text(self.logged_in_username_locator, expect_text)

    def click_cart_button(self) -> None:
        self.click_element(self.cart_button_locator)
