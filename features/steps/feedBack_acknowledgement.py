from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# The login step is already imported from common.py
# No need to define it again!

@when('I click on Supply Chain Management')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Supply Chain Management']"))
    ).click()

@when('I click the Pre-Procurement-Yarn')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Pre-Procurement-Yarn']"))
    ).click()

@when('I click the M&M Fabric Projection Acknowledgement')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='M&M Fabric Projection Acknowledgement']"))
    ).click()

@when('I click on the view icon')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='e-btn-icon fa fa-eye'])[1]"))
    ).click()

# --- Acknowledgment Scenario Specific ---
@when('I click on the acknowledge button')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='btnSave']"))
    ).click()

# --- Feedback Scenario Specific ---
@when('I click on the feedback button')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='btnUnAcknowledge']"))
    ).click()

@when('I click on the drop-down option and select the available reason')
def step_impl(context):
    # Open the dropdown container
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#select2-UnacknowledgeReasonID-container"))
    ).click()

    # Wait for the dropdown options to appear and select the one containing "Test-1"
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//li[contains(@class,'select2-results__option') and contains(text(), 'Test-1')]"))
    ).click()

@when('I click on the OK button')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='btnUnAckReasonSubmit']"))
    ).click()

# --- Common Validation Step ---
from selenium.common.exceptions import TimeoutException

@then('I should see a "Save successfully" message')
def step_impl(context):
    try:
        toast = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='toast-message']"))
        )

        message_text = toast.text.strip()
        print(f"[Toast Message] => '{message_text}'")

        # Accept common success variants
        expected_keywords = ["save successfully", "saved successfully", "successfully saved"]
        assert any(kw in message_text.lower() for kw in expected_keywords), \
            f"Expected success message but got: '{message_text}'"

    except TimeoutException:
        context.driver.save_screenshot('toast_not_found.png')
        raise AssertionError("Toast message did not appear within timeout.")

    except Exception as e:
        context.driver.save_screenshot('toast_error.png')
        raise AssertionError(f"Unexpected error during toast validation: {e}")


    context.driver.quit()
