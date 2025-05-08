import os
import time
import allure
from selenium import webdriver
from behave import *


# Make sure the screenshots folder exists inside allure-results
def create_screenshot_dir():
    screenshots_path = "allure-results/screenshots"
    if not os.path.exists(screenshots_path):
        os.makedirs(screenshots_path)
    return screenshots_path


# Initialize WebDriver before all scenarios
def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


# Quit WebDriver after all scenarios
def after_all(context):
    context.driver.quit()


# Capture screenshot after each step
def after_step(context, step):
    if context.driver:
        # Screenshot name based on the current step and timestamp
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshots_path = create_screenshot_dir()
        screenshot_path = f"{screenshots_path}/{step.name}_{timestamp}.png"

        # Save the screenshot
        context.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

        # Attach the screenshot to the Allure report
        allure.attach(
            open(screenshot_path, "rb").read(),
            name=f"Screenshot for step: {step.name}",
            attachment_type=allure.attachment_type.PNG
        )


# Capture screenshot if the scenario fails
def after_scenario(context, scenario):
    if scenario.status == 'failed' and context.driver:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshots_path = create_screenshot_dir()
        screenshot_path = f"{screenshots_path}/{scenario.name}_failed_{timestamp}.png"

        # Save the screenshot
        context.driver.save_screenshot(screenshot_path)
        print(f"Failure Screenshot saved at: {screenshot_path}")

        # Attach the screenshot to Allure for failed scenarios
        allure.attach(
            open(screenshot_path, "rb").read(),
            name=f"Failure Screenshot for scenario: {scenario.name}",
            attachment_type=allure.attachment_type.PNG
        )

# Create a directory for screenshots after all tests
def after_all(context):
    create_screenshot_dir()  # Ensure screenshots directory exists
    context.driver.quit()

