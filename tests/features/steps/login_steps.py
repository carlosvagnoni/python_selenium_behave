"""
login_steps.py - Behave Step Definitions for User Login

This file contains step implementations for a Behave scenario related to user login.
Each step corresponds to a specific action or verification in the login process.

Steps Defined:
    - 'the user has signed up with credentials: "{username}", "{password}".' - Stores provided signup credentials.
    - 'the user is on the Login Page.' - Navigates to the login page and takes a screenshot.
    - 'the user inputs their username and password into the form.' - Enters login credentials.
    - 'the user clicks on the Submit button.' - Submits the login form.
    - 'the user should be logged in.' - Verifies successful login.

This file encapsulates the step definitions for user login in a test scenario.
"""

from behave import *
from tests.utils.allure_reports import allure_screenshot_as_png


@given('the user has signed up with credentials: "{username}", "{password}".')
def step_implX(context, username, password):
    context.username = username
    context.password = password


@given('the user is on the Login Page.')
def step_implA(context):
    context.web.get(context.config['url'])
    context.base_page.click_login_button()
    context.base_page.wait_for_login_title()
    context.base_page.verify_login_title()
    allure_screenshot_as_png(context, "login_page")


@when("the user inputs their username and password into the form.")
def step_implB(context):
    context.base_page.enter_login_username(context.username)
    context.base_page.enter_login_password(context.password)


@step("the user clicks on the Submit button.")
def step_implC(context):
    context.base_page.submit_login()


@then("the user should be logged in.")
def step_impl(context):
    expected_text = f"Welcome {context.username}"
    context.base_page.wait_for_logged_in_username(expected_text)
    context.base_page.verify_logged_in_username(expected_text)
    allure_screenshot_as_png(context, "user_logged_in")
