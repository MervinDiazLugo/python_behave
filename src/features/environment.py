import json
import os

from src.factory import drivers_factory

########################
##    BEFORE-HOOKS    ##
########################

def before_all(context):
    context.variables = {}
    context.driver_type = "chrome"
    context.headless = False
    context.basedir = os.path.abspath(os.path.join(__file__, "../.."))

    if context.config.userdata["driver"]:
        context.driver_type = context.config.userdata["driver"]

    if context.config.userdata["headless"]:
        if context.config.userdata["headless"] == "True":
            context.headless = True
        else:
            context.headless = False

    with open(f'{context.basedir}/environments/{context.config.userdata["env"]}.json') as file:
        context.environment_variables = json.load(file)
        context.username = context.environment_variables["username"]
        context.password = context.environment_variables["password"]

def before_feature(context, feature):
    if "Google" in feature.tags:
        context.host = "https://www.google.com"
    elif "Orange" in feature.tags:
        context.host = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    else:
        assert False, "Unknown host"


def before_scenario(context, scenario):
    driver_factory = drivers_factory.WebDriverFactory()
    context.driver = driver_factory.get_driver(driver=context.driver_type, headless=context.headless)
    context.driver.get(context.host)

def before_step(context, step):
    pass

#######################
##    AFTER-HOOKS    ##
#######################

def after_all(context):
    pass
def after_feature(context, feature):
    pass
def after_scenario(context, scenario):
    context.driver.quit()
def after_step(context, step):
    pass