from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonFunctions:

    TIME_OUT = 30

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

    def wait(self, time_out=TIME_OUT):
        return WebDriverWait(self.driver, time_out)

    def get_page_title(self):
        title = self.driver.title
        return title

    def wait_element_present(self, element):
        try:
            self.wait().until(EC.presence_of_element_located(element))
        except TimeoutException:
            assert False,f"Element: {element} was not present"

    def wait_element_visible(self, element):
        try:
            self.wait().until(EC.presence_of_element_located(element))
        except TimeoutException:
            assert False, f"Element: {element} was not visible"

    def wait_element_invisible(self, element, time_out=TIME_OUT):
        WebDriverWait(self.driver, time_out).until(EC.invisibility_of_element_located(element))

    def wait_element_clickable(self, element, time_out=TIME_OUT):
        WebDriverWait(self.driver, time_out).until(EC.element_to_be_clickable(element))

    def find_element(self, element):
        element = self.driver.find_element(*element)
        return element

    def find_elements(self, element):
        elements = self.driver.find_elements(*element)
        return elements

    def click_element(self, element):
        self.wait_element_clickable(element)
        self.find_element(element).click()

    def send_keys(self, element, key):
        self.wait_element_visible(element)
        self.find_element(element).send_keys(key)