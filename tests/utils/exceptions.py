import logging
from selenium.common import (
    NoSuchElementException,
    StaleElementReferenceException,
    ElementNotVisibleException,
    ElementNotInteractableException,
    ElementClickInterceptedException,
    WebDriverException,
    TimeoutException,
    NoAlertPresentException,
    UnexpectedAlertPresentException
)

def handle_exception(logger, exception):
    logger.error(exception)
    raise

def exception_handler(func):
    """
        Decorator to handle common Selenium exceptions that may occur during function execution.
        Args:
            func: The function to be decorated.
        Returns:
            function: Decorated function with exception handling.
        """
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (
            NoSuchElementException,
            StaleElementReferenceException,
            ElementNotVisibleException,
            ElementNotInteractableException,
            ElementClickInterceptedException,
            TimeoutException,
            NoAlertPresentException,
            UnexpectedAlertPresentException,
            WebDriverException
        ) as e:
            logger = logging.getLogger(__name__)
            if isinstance(e, WebDriverException):
                logger.error("WebDriver exception occurred:")
            elif isinstance(e, TimeoutException):
                logger.error("Timeout expired")
            elif isinstance(e, NoAlertPresentException):
                logger.error("Alert not found.")
            else:
                logger.error(f"Element {e.__class__.__name__} occurred")
            handle_exception(logger, e)
    return inner_function
