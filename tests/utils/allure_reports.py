import allure
from allure_commons.types import AttachmentType


def allure_screenshot_as_png(context, name: str):
    """
    Attaches a screenshot to an Allure report.

    Args:
        context: behave context.
        name (str): Name to identify the screenshot in the report.
    """
    allure.attach(context.web.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)