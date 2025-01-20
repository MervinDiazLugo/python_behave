from selenium.webdriver.common.by import By
from src.utils.common_functions import CommonFunctions
from selenium.webdriver import Keys

class OrangePage(CommonFunctions):

    SEARCH_INPUT = (By.CSS_SELECTOR, "textarea[name=q]")

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGING_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    USER_BULLET = (By.CSS_SELECTOR, "img[alt='profile picture']")
    ADMIN_USER_TABLE_LIST = (By.CSS_SELECTOR, "div[class=oxd-table-card]")
    ADMIN_MODULE = (By.CSS_SELECTOR, "a[href='/web/index.php/admin/viewAdminModule']")

    def fill_user_name(self, username):
        if username != "":
            self.send_keys(self.USERNAME, username)
        else:
            assert False, f"username is empty"

    def fill_pass(self, password):
        if password != "":
            self.send_keys(self.PASSWORD, password)
        else:
            assert False, f"password is empty"

    def click_login(self):
        self.click_element(self.LOGING_BUTTON)

    def click_admin_module(self):
        self.click_element(self.ADMIN_MODULE)

    def verify_log_in(self):
        self.wait_element_present(self.USER_BULLET)
        assert self.find_element(self.USER_BULLET).is_displayed(), f"Can't log in to {self.USER_BULLET}"

    def get_system_user_list(self, user_name):
        self.wait_element_present(self.ADMIN_USER_TABLE_LIST)
        system_user_elm = self.find_elements(self.ADMIN_USER_TABLE_LIST)
        is_present = False
        if not system_user_elm.__len__() == 0:
            for elem in system_user_elm:
                current_username_data = elem.text.split("\n")
                if user_name in current_username_data:
                    is_present= True
                    break
            assert is_present != False, f"Can't find {user_name} in the list"
        else:
            assert False, "Admin table at main menu is not present";