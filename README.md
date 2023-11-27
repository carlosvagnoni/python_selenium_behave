# Automated Web Testing with Python, Selenium, and Behave 🤖🐍

This project provides a structure and tools for automated web testing using Python, Selenium, and Behave, following Behavior-Driven Development (BDD) best practices and employing the Page Object Model design pattern.

## Testing demoblaze.com Features 🧪

This suite of tests is specifically designed to validate and test features on the [demoblaze.com](https://www.demoblaze.com) website. You'll find feature files under the `tests/features` directory related to signup, login and adding products to the cart.

![python_selenium_behave](https://github.com/carlosvagnoni/python_selenium_behave/assets/106275103/b8213b2a-cde3-404f-96d7-84b45237a999)

## Table of Contents 📑

- [Requirements](#requirements-)
- [Folder Structure](#folder-structure-)
- [Installation](#installation-)
- [Configuration](#configuration-)
- [Test Execution](#test-execution-)
- [Contact](#contact-)

## Requirements 📋

- Python 3.10.11
- Selenium 4.15.2
- Behave 1.2.6
- Allure-Behave 2.13.2
- Webdriver Manager 4.0.1

## Folder Structure 📂

- **behave.ini:** Configuration file for Behave.
- **config.json:** Configuration file for variable data.
- **logging.conf:** Logging configuration.
- **requirements.txt:** List of dependencies and versions.
- **run.bat:** Script file specifically designed for execution in Windows environments.

### Directory "tests"

- **features:** Directory containing specification files in Gherkin format.
  - **environment.py:** Behave configuration file.
  - **steps:** Implementation of steps defined in the specifications.

- **pages:** Directory containing Page Object Model classes.

- **utils:** Directory containing common utilities for tests.
  - **allure_reports.py:** Method that attaches a screenshot to an Allure report..
  - **asserts.py:** Custom assertion functions.
  - **drivers.py:** Configuration and management of Selenium drivers.
  - **exceptions.py:** Decorator to handle common Selenium exceptions.
  - **page_object.py:** Definition of the base structure of the Page Object Model.

## Installation 🛠️

1. Clone this repository:

    ```bash
    git clone https://github.com/carlosvagnoni/python_selenium_behave.git
    cd python_selenium_behave
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration ⚙️

- Make sure you have a browser installed and configured in the script (Chrome, Edge, or Firefox).
- You can configure the config.json file to adjust parameters such as the base URL(url) or the desired browser to use(driver).

## Test Execution ▶️

Run all the tests:

```bash
behave -f allure_behave.formatter:AllureFormatter -o target\reports\allure_result
```

Open report:

```bash
allure serve target\reports\allure_result
```

**NOTE:**

- Set up the respective environment variables beforehand.
- On Windows environments, you can directly execute the `run.bat` file.

## Contact 📧

If you have any questions or suggestions, feel free to contact me through my social media accounts.

Thank you for your interest in this project!
