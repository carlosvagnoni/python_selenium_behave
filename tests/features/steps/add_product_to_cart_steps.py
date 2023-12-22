"""
add_product_to_cart_steps.py - Behave Step Definitions for Adding Products to Cart

This file defines step implementations for a Behave scenario related to adding products to a shopping cart.
Each step corresponds to a specific action or verification in the scenario.

Steps Defined:
    - 'the user is browsing the list of available products.' - Navigates to the main page and initializes page objects.
    - 'the user selects a product from the "laptops" category.' - Selects a laptop product from the category.
    - 'the user adds the selected product to the shopping cart.' - Adds the product to the cart and verifies success.
    - 'the product should be added to the user's shopping cart.' - Verifies the product in the shopping cart.

This file encapsulates the step definitions for adding products to the cart in a test scenario.
"""

from behave import given, when, step, then
from tests.utils.allure_reports import allure_screenshot_as_png
from tests.utils.asserts import Expect as expect
from tests.pages.home_page import HomePage
from tests.pages.product_page import ProductPage
from tests.pages.cart_page import CartPage
import logging


@given("the user is browsing the list of available products.")
def step_impl_browsing_products(context):
    try:
        expect(context.web.current_url).to_be_equal('https://www.demoblaze.com/')
    except AssertionError as e:
        logging.error(e)
        raise AssertionError
    allure_screenshot_as_png(context, "product_list")
    context.home_page = HomePage(context.web)
    context.product_page = ProductPage(context.web)
    context.cart_page = CartPage(context.web)


@when('the user selects a product from the "laptops" category.')
def step_impl_select_product(context):
    context.home_page.click_laptops_category_button()
    context.home_page.wait_for_macbook_button()
    context.home_page.click_macbook_button()


@step("the user adds the selected product to the shopping cart.")
def step_impl_add_to_cart(context):
    context.product_page.wait_for_macbook_title()
    context.product_page.click_add_to_cart()
    expected_text = 'Product added.'
    context.product_page.verify_alert_successful_added_to_cart(expected_text)
    context.product_page.submit_alert()


@then("the product should be added to the user's shopping cart.")
def step_impl_product_added(context):
    context.base_page.click_cart_button()
    context.cart_page.wait_for_macbook_title_in_cart()
    expected_text = 'MacBook air'
    context.cart_page.verify_macbook_title_in_cart(expected_text)
    allure_screenshot_as_png(context, "product_in_cart")
