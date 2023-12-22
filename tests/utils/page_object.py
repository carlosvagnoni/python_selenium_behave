import logging
from tests.utils.exceptions import exception_handler
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep as wait
from tests.utils.asserts import Expect as expect


class PageObject:
    """
    Base class representing the core functionalities and Selenium common methods used across Page Objects.
    All Page Objects inherit from this class.
    """
    def __init__(self, driver: WebDriver):
        """
        Initializes the PageObject with a WebDriver instance.
        Args:
            driver (WebDriver): WebDriver instance to interact with the browser.
        """
        self.web = driver

    # Selenium methods for common interactions with web elements
    @exception_handler
    def click_element(self, element_locator: tuple[str, str]) -> None:
        self.web.find_element(*element_locator).click()

    @exception_handler
    def wait_for_element_visibility(self, element_locator: tuple[str, str], timeout=10) -> WebElement | None:
        return WebDriverWait(self.web, timeout).until(EC.visibility_of_element_located(element_locator))

    @exception_handler
    def wait_for_element_presence(self, element_locator: tuple[str, str], timeout=10) -> WebElement | None:
        return WebDriverWait(self.web, timeout).until(EC.presence_of_element_located(element_locator))

    @exception_handler
    def wait_for_element_to_disappear(self, element_locator: tuple[str, str], timeout=10) -> WebElement | None:
        wait = WebDriverWait(self.web, timeout)
        return wait.until(EC.invisibility_of_element_located(element_locator))

    @exception_handler
    def wait_for_element_inner_text_to_be(self, element_locator: tuple[str, str], expected_text, timeout=10) -> bool | None:
        return WebDriverWait(self.web, timeout).until(
            EC.text_to_be_present_in_element(element_locator, expected_text)
        )

    @exception_handler
    def verify_element_text(self, element_locator: tuple[str, str], expected_text) -> None:
        try:
            expect(self.web.find_element(*element_locator).text).to_be_equal(expected_text)
        except AssertionError:
            actual_text = self.web.find_element(*element_locator).text
            error_message = f"Expected text to be '{expected_text}', but was '{actual_text}'"
            logging.error(AssertionError(error_message))
            raise AssertionError(error_message)

    @exception_handler
    def verify_element_text_value(self, element_locator: tuple[str, str], expected_text) -> None:
        try:
            expect(self.web.find_element(*element_locator).get_attribute('value')).to_be_equal(expected_text)
        except AssertionError:
            actual_text = self.web.find_element(*element_locator).get_attribute('value')
            error_message = f"Expected text to be '{expected_text}', but was '{actual_text}'"
            logging.error(AssertionError(error_message))
            raise AssertionError(error_message)

    @exception_handler
    def switch_to_alert(self) -> Alert | None:
        return self.web.switch_to.alert

    @exception_handler
    def verify_alert_text(self, expected_text) -> None:
        global alert_message
        try:
            alert = self.web.switch_to.alert
            alert_message = alert.text
            assert alert_message == expected_text
        except AssertionError:
            error_message = f"Assertion failed: Actual text '{alert_message}' does not match expected text '{expected_text}'"
            logging.error(AssertionError(error_message))
            raise AssertionError(error_message)

    @exception_handler
    def submit_alert(self) -> None:
        alert = self.web.switch_to.alert
        alert.accept()

    @exception_handler
    def enter_text(self, element_locator: tuple[str, str], text: str) -> None:
        self.web.find_element(*element_locator).send_keys(text)

    def wait_for_seconds(self, seconds: int) -> None:
        wait(seconds)

    @exception_handler
    def current_url(self) -> str | None:
        return self.web.current_url
