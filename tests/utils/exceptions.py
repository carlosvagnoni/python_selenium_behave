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
        except (NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException) as e:
            logging.debug("Element not found or not visible")
            logging.debug(e)
        except ElementNotInteractableException as e:
            logging.debug("Element not interactable")
            logging.debug(e)
        except ElementClickInterceptedException as e:
            logging.debug("Element click intercepted")
            logging.debug(e)
        except TimeoutException:
            logging.debug("Timeout expired")
        except NoAlertPresentException as e:
            logging.debug("Alert not found.")
            logging.debug(e)
        except UnexpectedAlertPresentException as e:
            logging.debug("Unexpected alert.")
            logging.debug(e)
        except WebDriverException as e:
            logging.debug("WebDriver exception occurred:")
            logging.debug(e)

    return inner_function