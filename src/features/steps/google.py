from behave import *
from time import sleep
from src.pages.google_page import GooglePage

@step("A topic to find '{topic}'")
def step_impl(context, topic):
    context.current_page = GooglePage(context.driver)
    context.current_page.open(context.host)
    context.current_page.search(topic)
    sleep(5)