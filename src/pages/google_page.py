from selenium.webdriver.common.by import By
from src.utils.common_functions import CommonFunctions
from selenium.webdriver import Keys

class GooglePage(CommonFunctions):

    SEARCH_INPUT = (By.CSS_SELECTOR, "textarea[name=q]")

    def search(self, text):
        self.send_keys(self.SEARCH_INPUT, text)
        self.send_keys(self.SEARCH_INPUT, Keys.ENTER)