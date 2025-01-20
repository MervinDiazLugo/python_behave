from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


class WebDriverFactory:

    @staticmethod
    def get_driver(driver, headless):
        drivers = {"chrome": chrome(headless), "firefox": "", "edge": "", "opera": ""}
        return drivers[driver]


def chrome(headless):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--disable-application-cache")

    if headless:
        chrome_options.add_argument("--headless")
    else:
        chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    return driver