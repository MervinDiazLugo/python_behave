from behave import *
from src.pages.orange_page import OrangePage
use_step_matcher("re")


@step("The User fill username text box")
def step_impl(context):
    context.current_page = OrangePage(context.driver)
    context.current_page.fill_user_name(context.username)


@step("The User fill password text box")
def step_impl(context):
    context.current_page = OrangePage(context.driver)
    context.current_page.fill_pass(context.password)


@when("The User clicks Login button")
def step_impl(context):
    context.current_page = OrangePage(context.driver)
    context.current_page.click_login()


@then("Verify the user is logged in")
def step_impl(context):
    context.current_page = OrangePage(context.driver)
    context.current_page.verify_log_in()


@given("the user is Logged in")
def step_impl(context):
    context.current_page = OrangePage(context.driver)
    context.current_page.fill_user_name(context.username)
    context.current_page.fill_pass(context.password)
    context.current_page.click_login()
    context.current_page.verify_log_in()


@step("The user go to System user list")
def step_impl(context):
    context.current_page = OrangePage(context.driver)
    context.current_page.click_admin_module()


@when("Verify (.*) user is present in the list")
def step_impl(context, username):
     context.current_page = OrangePage(context.driver)
     context.current_page.get_system_user_list(username)