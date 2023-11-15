"""
signup_steps.py - Behave Step Definitions for User Registration

This file contains step implementations for a Behave scenario related to user registration.
Each step corresponds to a specific action or verification in the registration process.

Steps Defined:
    - 'the user is on the Registration Page.' - Navigates to the registration page and takes a screenshot.
    - 'the user provides the following registration details: "{username}", "{password}".' - Enters registration details and takes a screenshot.
    - 'the user clicks on the Sign Up button.' - Submits the registration form.
    - 'the user should be registered successfully.' - Verifies successful registration.

This file encapsulates the step definitions for user registration in a test scenario.
"""

from behave import *
from tests.utils.allure_reports import allure_screenshot_as_png


@given('the user is on the Registration Page.')
def step_implX(context):
    context.web.get(context.config['url'])
    context.base_page.click_signup_button()
    context.base_page.wait_for_signup_title()
    context.base_page.verify_signup_title()
    allure_screenshot_as_png(context, "signup_page")


@when('the user provides the following registration details: "{username}", "{password}".')
def step_implA(context, username, password):
    context.username = username
    context.password = password
    context.base_page.enter_signup_username(context.username)
    context.base_page.enter_signup_password(context.password)
    context.base_page.verify_entered_credentials(context.username, context.password)
    allure_screenshot_as_png(context, "entered_signup_credentials")


@step("the user clicks on the Sign Up button.")
def step_implB(context):
    context.base_page.submit_signup()


@then("the user should be registered successfully.")
def step_impl(context):
    expected_text = 'Sign up successful.'
    context.base_page.switch_to_alert()
    context.base_page.verify_alert_successful_signup(expected_text)
    context.base_page.submit_alert()


