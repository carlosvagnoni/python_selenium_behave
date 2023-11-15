from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options as ChromeOpt
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOpt
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOpt
from webdriver_manager.firefox import GeckoDriverManager

class Drivers:
    """
    The Drivers class manages the creation of different WebDriver instances for various browsers like Chrome, Edge, and Firefox.
    """
    def __init__(self, webdriver_type: str, isHeadless=False) -> None:
        """
        Initializes a Drivers instance using the provided WebDriver type, defaulting headless mode to false.
        :param webdriver_type: The type of WebDriver to initialize (e.g., "chrome", "edge", "firefox")
        :param isHeadless: Flag indicating whether to run the browser in headless mode
        """
        self.isHeadless = isHeadless
        self.driver = self.get_webdriver(webdriver_type)

    def get_webdriver(self, webdriver_type: str):
        """
        Gets the appropriate WebDriver based on the specified type.
        :param webdriver_type: The type of WebDriver to initialize (e.g., "chrome", "edge", "firefox")
        :return: instance for the specified browser type
        """
        match webdriver_type:
            case 'chrome':
                return self.chromeDriver()
            case 'edge':
                return self.edgeDriver()
            case 'firefox':
                return self.firefoxDriver()
            case _:
                raise ValueError(f"Unsupported webdriver_type: {webdriver_type}")

    def chromeDriver(self):
        # Creating an instance of Chrome
        if self.isHeadless == True:
            execution = ChromeOpt()
            execution.add_argument("--headless")
            return webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()), options=execution)
        else:
            return webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

    def edgeDriver(self):
        # Creating an instance of Microsoft Edge
        if self.isHeadless == True:
            execution = EdgeOpt()
            execution.add_argument("--headless")
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=execution)
        else:
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    def firefoxDriver(self):
        # Creating an instance of Firefox
        if self.isHeadless == True:
            execution = FirefoxOpt()
            execution.add_argument("--headless")
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=execution)
        else:
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

