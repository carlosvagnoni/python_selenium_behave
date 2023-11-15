"""
environment.py - Behave Test Environment Configuration

This file contains the environment setup and teardown methods for Behave tests. It defines functions
that are executed before and after different test stages (all tests, features, scenarios, steps) to
prepare the testing environment, handle test execution, and clean up resources.

Functions:
    - before_all(context): Executes before all test runs, initializes logging and loads configuration.
    - before_feature(context, feature): Runs before each feature test scenario.
    - before_scenario(context, scenario): Executes before each scenario test.
    - before_step(context, step): Executed before each step within a scenario.
    - after_step(context, step): Runs after each step, logs step status, handles failures, and quits the web driver.
    - after_scenario(context, scenario): Executed after each scenario, logs scenario status, and quits the web driver.
    - after_feature(context, feature): Runs after each feature, logs feature status.
    - after_all(context): Executed after all tests, shuts down the logging system.

This file encapsulates the setup and teardown procedures necessary for Behave tests, initializing the
environment, managing the web driver, and logging events throughout the test execution.
"""

import json
import allure
from allure_commons.types import AttachmentType
from selenium.common import UnexpectedAlertPresentException
from tests.pages.base_page import BasePage
from tests.utils.drivers import Drivers
import logging.config


def before_all(context):
    logging.config.fileConfig('logging.conf')
    logging.info('Running python_selenium_behave project...')
    with open('config.json') as config_file:
        context.config = json.load(config_file)


def before_feature(context, feature):
    logging.info(f'Starting FEATURE: {feature.name}')


def before_scenario(context, scenario):
    logging.info(f'Running SCENARIO: {scenario.name}')
    context.web = Drivers(context.config['driver']).driver
    context.web.maximize_window()
    context.base_page = BasePage(context.web)


def before_step(context, step):
    logging.info(f'Running STEP: {step.name}')


def after_step(context, step):
    logging.info(f'Finished STEP: {step.name}')
    match step.status:
        case 'skipped':
            logging.debug('This step was skipped during testing.')
        case 'passed':
            logging.debug('The step was tested successfully.')
        case 'failed':
            logging.debug('The step failed.')
            try:
                allure.attach(context.web.get_screenshot_as_png(), name="fail_scenario",
                              attachment_type=AttachmentType.PNG)
            except UnexpectedAlertPresentException:
                logging.debug("Unexpected alert")
            finally:
                context.web.quit()


def after_scenario(context, scenario):
    logging.info(f'Finished SCENARIO: {scenario.name}')
    match scenario.status:
        case 'skipped':
            logging.debug('One or more steps of this scenario was passed over during testing.')
        case 'passed':
            logging.debug('The scenario was tested successfully.')
        case 'failed':
            logging.debug('One or more steps of this scenario failed.')

    if context.web is not None:
        context.web.quit()


def after_feature(context, feature):
    logging.info(f'Finished FEATURE: {feature.name}')
    match feature.status:
        case 'skipped':
            logging.debug('One or more steps of this feature was passed over during testing.')
        case 'passed':
            logging.debug('The feature was tested successfully.')
        case 'failed':
            logging.debug('One or more steps of this feature failed.')


def after_all(context):
    logging.shutdown()
