import logging
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException, \
    ElementNotInteractableException, ElementClickInterceptedException, WebDriverException, TimeoutException, \
    NoAlertPresentException, UnexpectedAlertPresentException


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
        except NoSuchElementException as e:
            logging.error("Element not found")
            logging.error(e)
            raise
        except StaleElementReferenceException as e:
            logging.error("Element not visible")
            logging.error(e)
            raise
        except ElementNotVisibleException as e:
            logging.error("Element not visible")
            logging.error(e)
            raise
        except ElementNotInteractableException as e:
            logging.error("Element not interactable")
            logging.error(e)
            raise
        except ElementClickInterceptedException as e:
            logging.error("Element click intercepted")
            logging.error(e)
            raise
        except TimeoutException:
            logging.error("Timeout expired")
            raise
        except NoAlertPresentException as e:
            logging.error("Alert not found.")
            logging.error(e)
            raise
        except UnexpectedAlertPresentException as e:
            logging.error("Unexpected alert.")
            logging.error(e)
            raise
        except WebDriverException as e:
            logging.error("WebDriver exception occurred:")
            logging.error(e)
            raise

    return inner_function
