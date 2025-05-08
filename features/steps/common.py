from behave import given
from selenium import webdriver
from pages.loginTexlieERP import LoginPage

@given('I am on the dashboard page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    login_page = LoginPage(context.driver)
    login_page.load()
    login_page.login("mahmud.ip", "Mahmud12#")
